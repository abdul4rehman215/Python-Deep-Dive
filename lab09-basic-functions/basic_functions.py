# Define a greeting function
def greet(name):
    return f"Hello, {name}!"

# Call the function
print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))

# Function with default parameter
def greet_default(name="Guest"):
    return f"Hello, {name}!"

print(greet_default())

# Using keyword argument
print(greet_default(name="Diana"))
