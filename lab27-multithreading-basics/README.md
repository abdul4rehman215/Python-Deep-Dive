# 🧪 Lab 27: Multithreading Basics 🧵

## 🎯 Objectives
- Understand the fundamentals of multithreading in Python
- Learn how to create and run threads using the threading module
- Observe concurrent execution of threads
- Understand shared memory and basic concurrency issues

---

## 📌 Prerequisites
- Basic knowledge of Python programming
- Familiarity with functions and loops
- Python 3.x installed

---

## 📖 Introduction
Multithreading allows a program to execute multiple tasks concurrently within the same process.
In Python, threads share the same memory space, which enables fast communication but can also lead to concurrency issues such as race conditions.
This lab demonstrates how to create, start, and synchronize threads using Python’s built-in `threading` module.

---

## 🧩 Lab Tasks

### 🔹 Task 1: Import the threading Module
- Use the built-in `threading` module to manage threads

### 🔹 Task 2: Define a Thread Function
- Create a function that will be executed by multiple threads

### 🔹 Task 3: Create and Start Threads
- Instantiate multiple threads with different arguments
- Start threads using `start()`

### 🔹 Task 4: Synchronize Threads
- Use `join()` to wait for thread completion

---

## 🧠 Key Concepts Learned
- Thread creation and execution
- Concurrent execution flow
- Shared memory model
- Thread synchronization using `join()`
- Non-deterministic execution order

---

## ✅ Conclusion
This lab introduced the basics of multithreading in Python.
You learned how to create threads, run tasks concurrently, and synchronize execution.
Multithreading is useful for improving performance in I/O-bound tasks, but it must be handled carefully to avoid race conditions and data inconsistency.
