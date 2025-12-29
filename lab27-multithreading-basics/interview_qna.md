# 📘 Interview Q&A – Lab 27: Multithreading Basics

1. **What is multithreading?**  
   Multithreading allows multiple tasks to run concurrently within the same process.

2. **Which Python module is used for multithreading?**  
   The built-in `threading` module.

3. **How do you create a thread in Python?**  
   By creating a `threading.Thread` object with a target function.

4. **What does the start() method do?**  
   It begins execution of the thread.

5. **Why is join() used in threading?**  
   It makes the main program wait until the thread finishes execution.

6. **Do threads share memory in Python?**  
   Yes, all threads share the same memory space.

7. **Why can thread output order vary?**  
   Because thread scheduling is managed by the operating system.

8. **What is a race condition?**  
   When multiple threads access shared data simultaneously without synchronization.
