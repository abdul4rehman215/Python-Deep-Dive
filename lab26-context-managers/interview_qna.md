# 📘 Interview Q&A – Lab 26: Context Managers

1. **What is a context manager in Python?**  
   A context manager automatically manages setup and cleanup of resources.

2. **Which keyword is used with context managers?**  
   The `with` statement.

3. **Which method runs when entering a context?**  
   The `__enter__()` method.

4. **Which method runs when exiting a context?**  
   The `__exit__()` method.

5. **Why is `__exit__()` important?**  
   It ensures cleanup even if an exception occurs.

6. **What arguments does `__exit__()` receive?**  
   Exception type, value, and traceback.

7. **Why are context managers preferred over manual cleanup?**  
   They reduce errors and ensure reliable resource handling.

8. **Give one real-world use case of context managers.**  
   File handling or database connections.
