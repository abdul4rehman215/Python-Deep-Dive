import requests

# Send a GET request to the GitHub API
response = requests.get("https://api.github.com")

# Print HTTP status code
print("Status Code:", response.status_code)

# Parse JSON response
data = response.json()
print("\nFull JSON Response (truncated):")
print(dict(list(data.items())[:5]))

# Access specific fields safely
print("\nAccessing specific fields:")
print("User URL:", data.get("current_user_url"))
print("Repository Search URL:", data.get("repository_search_url"))
