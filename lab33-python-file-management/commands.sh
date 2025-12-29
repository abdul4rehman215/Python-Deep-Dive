#!/bin/bash
# Lab 33 - File Management with Python

# Create source directory and files
mkdir source_folder
echo "Sample file 1" > source_folder/file1.txt
echo "Sample file 2" > source_folder/file2.log

# Run the Python script
python3 file_management.py

# Verify copied files
ls backup_folder
