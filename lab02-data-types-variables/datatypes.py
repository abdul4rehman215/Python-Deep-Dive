# Creating variables of different data types
name = "John Doe"
age = 25
is_student = True
height = 175.5

# Printing variables and their types
print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age))
print("Is Student:", is_student, "Type:", type(is_student))
print("Height:", height, "Type:", type(height))

# Implicit type casting
a = 10
b = 10.5
result = a + b
print("Result:", result, "Type:", type(result))

# Explicit type casting
age_str = str(age)
print("Age as string:", age_str, "Type:", type(age_str))

number_str = "100"
number_int = int(number_str)
print("Number:", number_int, "Type:", type(number_int))

# Case study: customer data intake
customer_name = "Alice Johnson"
customer_age = "30"
customer_membership = "True"

customer_age = int(customer_age)
customer_membership = customer_membership == "True"

print("Customer Name:", customer_name, "Type:", type(customer_name))
print("Customer Age:", customer_age, "Type:", type(customer_age))
print("Customer Membership Status:", customer_membership, "Type:", type(customer_membership))
