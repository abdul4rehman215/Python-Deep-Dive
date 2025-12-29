# lambda_functions.py

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() with lambda
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled Numbers:", doubled)

# filter() with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# reduce() with lambda
total_sum = reduce(lambda x, y: x + y, numbers)
print("Sum of Numbers:", total_sum)
