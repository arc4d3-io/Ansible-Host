import subprocess
import yaml
from models.logger import Logger

class AnsibleHost:

    def __init__(self, host_file):
        self.host_file = host_file
        self.hosts = None
        self.groups = None
        self.ip = None
        self.hostname = None
        self.target = None
        self.logger = Logger()

        self._load_inventory()
        self._get_groups()

    def _write_hosts_yaml(self):
        with open(self.host_file, 'w') as file:
            yaml.safe_dump(self.hosts, file)
        self.logger.log(f"OK - [{self.ip}] [{self.hostname}] salvo no grupo [{self.target}]")                              
        return True

    def _set_host_to_group(self):
        group = self.hosts[self.target]['hosts']
        group[self.hostname] = {'ansible_host': self.ip}
        self._write_hosts_yaml()

    def _set_new_group(self):
        current_dict = self.hosts
        group_parts = self.target.split('.')
        for part in group_parts:
            if part not in current_dict:
                current_dict[part] = {'hosts': {}}
            current_dict = current_dict[part]['hosts']
        current_dict[self.hostname] = {'ansible_host': self.ip}
        self._write_hosts_yaml()

    def _get_groups(self):
        self.groups = self.hosts.keys()

    def _load_inventory(self):
        with open(self.host_file, 'r') as file:
            self.hosts = yaml.safe_load(file)

    def _get_hostname_from_ip(self):
        hostname = subprocess.check_output(["dig", "+short", "-x", self.ip]).decode("utf-8").strip()
        return hostname[:-1] if hostname.endswith(".") else hostname

    def _prompt_client_ip(self):
        self.ip = input("\n1 - Informe o IP da máquina que deseja cadastrar: ")
        self.hostname = self._get_hostname_from_ip()

    def _prompt_client_hostname(self):
        msg = f"\nHostname encontrado para o IP [{self.ip}] é [{self.hostname}]\n"
        print(msg)
        answer = input("\n2 - Deseja usar esse hostname (h) ou cadastrar o IP (i): ")
        if not answer.lower().startswith("h"):
            self.hostname = self.ip

    def _prompt_client_target_group(self):
        self.target = input("\n3 - Em qual grupo deseja cadastrar a máquina: ")
        if self.target in self.groups:
            msg = f"\nGrupo [{self.target}] selecionado\n"
            print(msg)
            answer = input(f"\n4 - Confirmar e salvar (s/n): ")
            if answer.lower().startswith("s"):
                self._set_host_to_group()
            else:
                self.ask()
        else:
            self._prompt_client_create_new_group()

    def _prompt_client_create_new_group(self):
        msg = f"\nO grupo [{self.target}] não existe.\n"
        print(msg)
        answer = input(f"\n4 - Criar um novo grupo com esse nome (s/n): ")
        if answer.lower().startswith("s"):
            self._set_new_group()
        else:
            self.ask()

    def _display_groups(self):
        print(f"Arquivo host [{self.host_file}]\nGrupos de hosts existentes:\n")
        for group in self.groups:
            print(f"- {group}")

    def ask(self):
        self._prompt_client_ip()
        self._prompt_client_hostname()
        self._display_groups()        
        self._prompt_client_target_group()
        return True

    def get_ip(self):
        return self.ip
       