#!/bin/bash
# Lab 21 - Reading CSV Files

# Step 1: Create sample CSV file
cat > sample.csv << EOF
name,age,city
Alice,30,New York
Bob,25,London
Charlie,35,Sydney
EOF

# Step 2: Create Python script
nano read_csv.py

# Step 3: Run Python script
python3 read_csv.py
