# Azure Sentinel Analytic Rule Deletion Script

This Python script automates the deletion of Azure Sentinel analytic rules by name, using a list of rule names provided in a text file. It utilizes Azure CLI commands under the hood to fetch rule IDs and then delete the specified rules in a bulk operation.
## Features
* Loads rule names to delete from a text file.
* Fetches all analytic rules from a specified Azure Sentinel workspace.
* Deletes rules whose names match those specified in the text file.

## Prerequisites
* Azure CLI: Make sure Azure CLI is installed and you are logged in to your Azure account (use az login).
* Python 3.x: Ensure Python is installed on your system.
* Permissions: The executing Azure account must have permissions to list and delete analytic rules in the specified Azure Sentinel workspace.

## Usage

* Prepare Rule Names File: Create a text file named ana (or any name of your choice, but make sure to update the script accordingly) and list the names of the Azure Sentinel analytic rules you wish to delete, each on a new line.

* Configure the Script: Open the script and set the resource_group, workspace, and rules_file_path variables to match your Azure Sentinel workspace details and the path to your rules file.

* Run the Script: Execute the script in your terminal or command prompt:
`python delete_sentinel_rules.py`

## How It Works

* The script reads the names of rules to be deleted from the specified text file.
* It then lists all current analytic rules in the specified Azure Sentinel workspace.
* For each rule listed in the text file, the script finds a matching rule by name in the workspace and deletes it.

## Caution

This script performs deletions based on exact matches to rule names. Ensure the rule names in your text file are correct and match exactly those in Azure Sentinel.  
Always back up or review rules before running this script, as deletions cannot be undone.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements, bug fixes, or feature requests.

### License  
This project is licensed under the MIT License - see the LICENSE file for details.