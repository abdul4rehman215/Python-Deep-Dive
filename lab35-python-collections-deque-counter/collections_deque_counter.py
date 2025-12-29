from collections import deque, Counter

# ----- deque example -----
d = deque()

d.append("task1")
d.append("task2")

last_task = d.pop()
print("Popped from the right:", last_task)

d.appendleft("task0")

first_task = d.popleft()
print("Popped from the left:", first_task)

# ----- Counter example -----
words = ["apple", "orange", "banana", "apple", "orange", "apple"]

word_count = Counter(words)
print("Word Count:", word_count)

most_common = word_count.most_common(2)
print("Most Common Words:", most_common)
