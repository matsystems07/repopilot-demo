```python
# main.py
"""
Open-Source Project Launch System

This script provides a command-line interface for launching and managing open-source projects.
It includes features for repository scaffolding, documentation generation, GitHub setup, and issue planning.

Usage:
    python main.py --help
"""

import os
import argparse
import subprocess
import shutil
import json
from datetime import datetime

# Define constants
PROJECT_NAME = "my_open_source_project"
REPO_URL = f"https://github.com/{PROJECT_NAME}.git"
README_TEMPLATE = "README.md.template"
ISSUE_TEMPLATE = "issue_template.md"

def scaffold_repository(project_name):
    """
    Create a new repository with basic structure.

    :param project_name: Name of the project
    """
    # Create project directory
    if not os.path.exists(project_name):
        os.makedirs(project_name)

    # Create subdirectories
    subdirectories = ["src", "docs", "tests"]
    for subdirectory in subdirectories:
        os.makedirs(os.path.join(project_name, subdirectory), exist_ok=True)

    # Create README file
    with open(os.path.join(project_name, "README.md"), "w") as f:
        f.write(f"# {project_name}\n")

def generate_documentation(project_name):
    """
    Generate documentation for the project.

    :param project_name: Name of the project
    """
    # Create documentation directory
    docs_dir = os.path.join(project_name, "docs")
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    # Create documentation files
    with open(os.path.join(docs_dir, "getting_started.md"), "w") as f:
        f.write(f"# Getting Started with {project_name}\n")

def setup_github(project_name):
    """
    Set up GitHub repository for the project.

    :param project_name: Name of the project
    """
    # Create GitHub repository
    try:
        subprocess.run(["gh", "repo", "create", project_name, "--public"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating GitHub repository: {e}")

def plan_issues(project_name):
    """
    Plan issues for the project.

    :param project_name: Name of the project
    """
    # Create issues directory
    issues_dir = os.path.join(project_name, "issues")
    if not os.path.exists(issues_dir):
        os.makedirs(issues_dir)

    # Create issue files
    with open(os.path.join(issues_dir, "issue_1.md"), "w") as f:
        f.write("# Issue 1\n")

def main():
    parser = argparse.ArgumentParser(description="Open-Source Project Launch System")
    parser.add_argument("--project_name", help="Name of the project")
    parser.add_argument("--scaffold", action="store_true", help="Scaffold repository")
    parser.add_argument("--docs", action="store_true", help="Generate documentation")
    parser.add_argument("--github", action="store_true", help="Set up GitHub repository")
    parser.add_argument("--issues", action="store_true", help="Plan issues")
    args = parser.parse_args()

    if args.project_name:
        project_name = args.project_name
    else:
        project_name = PROJECT_NAME

    if args.scaffold:
        scaffold_repository(project_name)
        print(f"Repository scaffolding complete for {project_name}")

    if args.docs:
        generate_documentation(project_name)
        print(f"Documentation generation complete for {project_name}")

    if args.github:
        setup_github(project_name)
        print(f"GitHub setup complete for {project_name}")

    if args.issues:
        plan_issues(project_name)
        print(f"Issue planning complete for {project_name}")

if __name__ == "__main__":
    main()
```

### Example Usage

1. Run the script with the `--help` flag to see the available options:
   ```bash
python main.py --help
```

2. Scaffold a new repository:
   ```bash
python main.py --project_name my_project --scaffold
```

3. Generate documentation for the project:
   ```bash
python main.py --project_name my_project --docs
```

4. Set up a GitHub repository for the project:
   ```bash
python main.py --project_name my_project --github
```

5. Plan issues for the project:
   ```bash
python main.py --project_name my_project --issues
```

Note: This script assumes you have the `gh` command-line tool installed and configured for GitHub. You can install it using the following command:
```bash
brew install gh
```
or
```bash
sudo apt-get install gh
```
Also, make sure you have the necessary permissions to create a new GitHub repository.

This script provides a basic structure for launching and managing open-source projects. You can extend it to include more features and functionality as needed.