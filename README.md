# AnsibleHost Class

This is an AnsibleHost class written in Python, designed to manage hosts and groups in an Ansible inventory file. It provides functionality to interact with host IP addresses, hostnames, and group organization.

## Features

- Load and manage Ansible inventory YAML file
- Add hosts to existing groups or create new groups
- Retrieve hostnames from IP addresses using the `dig` command
- Interactive prompts for user input

## Usage

1. Import the `AnsibleHost` class in your script
2. Create an instance of the `AnsibleHost` class with the path to your inventory file
3. Use the `ask()` method to start the interactive process for adding hosts to groups

```python
from ansible_host import AnsibleHost

inventory_file = "path/to/your/inventory.yaml"
ansible_host = AnsibleHost(inventory_file)
ansible_host.ask()
```

## Methods

- `_write_hosts_yaml`: Write the updated inventory to the file
- `_set_host_to_group`: Add a host to the specified group
- `_set_new_group`: Create a new group and add the host to it
- `_get_groups`: Retrieve the list of existing groups
- `_load_inventory`: Load the inventory from the file
- `_get_hostname_from_ip`: Get the hostname from the IP address using the `dig` command
- `_prompt_client_ip`: Prompt the user for the IP address of the host
- `_prompt_client_hostname`: Prompt the user to confirm the hostname or use the IP address
- `_prompt_client_target_group`: Prompt the user for the target group to add the host to
- `_prompt_client_create_new_group`: Prompt the user to create a new group if the target group does not exist
- `_display_groups`: Display the list of existing groups
- `ask`: Start the interactive process to add hosts to groups
- `get_ip`: Get the IP address of the host

## Dependencies

- Python 3
- `subprocess`
- `yaml`
- `models.logger` (a custom logger module)