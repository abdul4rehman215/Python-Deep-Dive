# 📘 Interview Q&A – Lab 29: Basic SQLite Usage

1. **What is SQLite?**  
   SQLite is a lightweight, serverless, embedded relational database engine.

2. **Which Python module is used to work with SQLite?**  
   The built-in `sqlite3` module.

3. **What does sqlite3.connect(":memory:") do?**  
   It creates a temporary in-memory database stored in RAM.

4. **What is the purpose of a database cursor?**  
   A cursor executes SQL commands and retrieves query results.

5. **How do you create a table in SQLite?**  
   By executing a `CREATE TABLE` SQL statement.

6. **Why are parameterized queries important?**  
   They prevent SQL injection and improve security.

7. **What does executemany() do?**  
   It inserts multiple records efficiently in one operation.

8. **How are query results returned in Python?**  
   As a list of tuples.

9. **Why is connection.commit() necessary?**  
   It saves changes made to the database.

10. **Where is SQLite commonly used in real-world projects?**  
    In local apps, configuration storage, logging systems, and prototypes.
