#!/bin/bash

# Create module and main script
nano mymodule.py
nano main.py

# Create package structure
mkdir mypackage
touch mypackage/__init__.py
mv mymodule.py mypackage/

# Run the main script
python3 main.py
