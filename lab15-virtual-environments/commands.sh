#!/bin/bash

# Create project directory
mkdir my_project
cd my_project

# Create virtual environment
python3 -m venv myenv

# Activate virtual environment
source myenv/bin/activate

# Install a package
pip install requests

# Verify installed packages
pip list

# Deactivate environment
deactivate
