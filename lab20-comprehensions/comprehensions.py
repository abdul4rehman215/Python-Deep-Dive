# comprehensions.py

# List comprehension: squares of numbers
squares = [x ** 2 for x in range(10)]
print("Squares:", squares)

# Dictionary comprehension: word lengths
words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words}
print("Word Lengths:", word_lengths)

# Loop vs comprehension comparison
squares_loop = []
for x in range(10):
    squares_loop.append(x ** 2)

squares_comp = [x ** 2 for x in range(10)]

print("Loop Result:", squares_loop)
print("Comprehension Result:", squares_comp)
