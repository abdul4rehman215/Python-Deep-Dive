# ----- Using *args -----
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = add_numbers(1, 2, 3, 4, 5)
print("Sum using *args:", result)

# ----- Using **kwargs -----
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=30, city="New York")

# ----- Argument unpacking -----
numbers = [1, 2, 3, 4]
print("Sum using unpacked list:", add_numbers(*numbers))

data = {"name": "John", "age": 25}
show_info(**data)
