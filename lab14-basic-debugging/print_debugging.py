# print_debugging.py

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        print("DEBUG:", num, "added → total =", total)
    return total

numbers = [5, 10, 15]
result = calculate_sum(numbers)
print("Final Result:", result)
