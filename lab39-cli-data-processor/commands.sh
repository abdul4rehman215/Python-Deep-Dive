#!/bin/bash
# Lab 39 - CLI Data Processor

# Install dependency
pip install requests

# Run the CLI tool
python3 data_processor.py \
  --api_url https://api.github.com \
  --file_path output.json
