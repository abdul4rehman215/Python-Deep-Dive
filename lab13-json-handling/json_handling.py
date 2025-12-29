# json_handling.py

import json

# Python dictionary
employee_data = {
    "name": "John Doe",
    "age": 30,
    "department": "Engineering",
    "skills": ["Python", "Django", "Machine Learning"]
}

# Convert dictionary to JSON string
employee_json = json.dumps(employee_data, indent=4)
print(employee_json)

# Write JSON to file
with open("employee_data.json", "w") as f:
    f.write(employee_json)

# Read JSON from file
with open("employee_data.json", "r") as f:
    data = json.load(f)
    print(data)
