# Initialize a dictionary with user profile data
user_profile = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(user_profile)

# Access a value
print("User's Name:", user_profile["name"])

# Update a value
user_profile["age"] = 31
print("Updated User Profile:", user_profile)

# Remove a key-value pair
user_profile.pop("city")
print("Profile after removing city:", user_profile)

# Iterate over key-value pairs
for key, value in user_profile.items():
    print(f"{key}: {value}")

# Iterate over keys
for key in user_profile.keys():
    print("Key:", key)
