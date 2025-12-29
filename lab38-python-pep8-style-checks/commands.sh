#!/bin/bash
# Lab 38 - Python Style & PEP 8 Checks

# Install required tools
pip install flake8 black autopep8

# Run flake8 to detect issues
flake8 example.py

# Format code using black
black example.py

# Format code using autopep8
autopep8 --in-place --aggressive --aggressive example.py
