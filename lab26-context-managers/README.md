# 🧪 Lab 26: Context Managers (with statement) 🔁

## 🎯 Objectives
- Understand what context managers are in Python
- Learn how the `with` statement works internally
- Create a custom context manager using `__enter__` and `__exit__`
- Use context managers for safe resource handling

---

## 📌 Prerequisites
- Basic Python programming knowledge
- Familiarity with file handling and exceptions
- Python 3.x installed

---

## 📖 Introduction
Context managers in Python simplify resource management by ensuring that setup and cleanup logic is handled automatically.
They are commonly used for:
- File handling
- Database connections
- Locks and synchronization
- Network resources

The `with` statement guarantees that resources are released properly, even if an error occurs.

---

## 🧩 Lab Tasks

### 🔹 Task 1: Understand Context Manager Lifecycle
- `__enter__()` → runs at the start of the `with` block
- `__exit__()` → runs when exiting the block (even on exceptions)

### 🔹 Task 2: Create a Custom Context Manager
- Define a class with `__enter__` and `__exit__`
- Print messages to observe execution flow

### 🔹 Task 3: Use Context Manager for File Handling
- Automatically open and close a file
- Avoid manual cleanup code

---

## 🧠 Key Concepts Learned
- Context manager lifecycle
- `with` statement mechanics
- Automatic resource cleanup
- Exception-safe programming
- Cleaner and more reliable code

---

## ✅ Conclusion
This lab demonstrated how context managers work internally and why they are essential for safe resource handling.
By using the `with` statement and implementing `__enter__` and `__exit__`, you can write cleaner, safer, and more maintainable Python code.
Context managers are a core concept used extensively in real-world Python applications.
