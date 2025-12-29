# 🧪 Lab 28: Multiprocessing Basics ⚙️

## 🎯 Objectives
- Understand multiprocessing in Python
- Learn how to create and manage multiple processes
- Differentiate between threading and multiprocessing
- Execute CPU-bound tasks in parallel

---

## 📌 Prerequisites
- Basic Python programming knowledge
- Familiarity with threading concepts
- Python 3.x installed

---

## 📖 Introduction
Multiprocessing allows Python programs to run tasks in parallel using **separate processes**, each with its own memory space.
Unlike threads, processes bypass Python’s Global Interpreter Lock (GIL), making multiprocessing ideal for **CPU-bound tasks**.
This lab demonstrates how to create and run multiple processes using Python’s built-in `multiprocessing` module.

---

## 🧩 Lab Tasks

### 🔹 Task 1: Import the multiprocessing Module
- Use Python’s built-in `multiprocessing` module

### 🔹 Task 2: Define a CPU-Bound Function
- Create a function that performs heavy computation

### 🔹 Task 3: Create and Run Processes
- Spawn multiple processes
- Start and synchronize them using `start()` and `join()`

### 🔹 Task 4: Observe Parallel Execution
- Verify that processes run independently
- Understand memory isolation

---

## 🧠 Key Concepts Learned
- Process-based parallelism
- CPU-bound vs I/O-bound tasks
- Process isolation and memory separation
- Importance of `if __name__ == "__main__":`
- True parallel execution across CPU cores

---

## ✅ Conclusion
This lab introduced multiprocessing as a solution for CPU-intensive workloads.
You learned how to create independent processes, run tasks in parallel, and understand why multiprocessing outperforms threading for heavy computation.
Multiprocessing is essential for performance-critical Python applications such as data processing, analytics, and scientific computing.
