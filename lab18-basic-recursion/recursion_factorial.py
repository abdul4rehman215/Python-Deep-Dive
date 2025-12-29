# recursion_factorial.py

# Recursive factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Iterative factorial
def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Tail recursion example
def tail_recursive_factorial(n, accumulator=1):
    if n <= 1:
        return accumulator
    return tail_recursive_factorial(n - 1, n * accumulator)

# Test values
number = 5

print("Recursive factorial:", factorial(number))
print("Iterative factorial:", iterative_factorial(number))
print("Tail recursive factorial:", tail_recursive_factorial(number))
