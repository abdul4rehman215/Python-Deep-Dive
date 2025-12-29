# 📘 Interview Q&A – Lab 28: Multiprocessing Basics

1. **What is multiprocessing in Python?**  
   Multiprocessing runs tasks in parallel using separate processes.

2. **Which Python module supports multiprocessing?**  
   The built-in `multiprocessing` module.

3. **Why is multiprocessing preferred for CPU-bound tasks?**  
   It enables true parallelism and bypasses the GIL.

4. **How do you create a new process?**  
   By creating a `multiprocessing.Process` object.

5. **What does the start() method do?**  
   It launches the process and begins execution.

6. **Why is join() important in multiprocessing?**  
   It ensures the main program waits until the process completes.

7. **Why is `if __name__ == "__main__":` required?**  
   To prevent infinite child process creation.

8. **Do processes share memory by default?**  
   No, each process has its own isolated memory.
