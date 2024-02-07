import json
import subprocess

# Replace these variables with your actual details
resource_group = 'resource-group-name'
workspace = 'workspace-name'
# Path to the file containing the display names of the rules to delete (new line separated)
rules_file_path = 'path/to/rules.txt' 

def run_az_command(command):
    """Run Azure CLI command."""
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

def get_rules(resource_group, workspace):
    """Get all analytic rules in a Sentinel workspace."""
    command = f'az sentinel alert-rule list --resource-group {resource_group} --workspace-name {workspace}'
    output = run_az_command(command)
    return json.loads(output)

def delete_rule(rule_id, resource_group, workspace):
    """Delete a specific analytic rule by ID."""
    command = f'az sentinel alert-rule delete --name {rule_id} -g {resource_group} -w {workspace} --yes'
    output = run_az_command(command)
    print(f'Deleted rule {rule_id}: {output}')  # Print command output for debugging

def load_rules_to_delete(file_path):
    """Load rules to delete from a file."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def main():
    # Load rules to delete from the specified file
    rules_to_delete = load_rules_to_delete(rules_file_path)

    # Fetch all rules
    rules = get_rules(resource_group, workspace)

    # Iterate over each rule and delete if the displayName matches one of the targeted rules
    for rule in rules:
        if rule.get('displayName', '').strip() in rules_to_delete:
            print(f"Found rule to delete: {rule['displayName']}")
            delete_rule(rule['name'], resource_group, workspace)
        # uncomment the else block to see which rules are skipped
        #else:
        #    print(f"Skipping rule: {rule.get('displayName', 'No displayName found')}")

if __name__ == '__main__':
    main()
