import sqlite3

# Connect to an in-memory SQLite database
connection = sqlite3.connect(":memory:")

# Create a cursor
cursor = connection.cursor()

# Create a table
cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade REAL
)
""")

# Insert records into the table
students_data = [
    (1, "Alice", 85.5),
    (2, "Bob", 78.0),
    (3, "Charlie", 92.0)
]

cursor.executemany(
    "INSERT INTO students VALUES (?, ?, ?)",
    students_data
)

# Commit changes
connection.commit()

# Query the table
cursor.execute("SELECT * FROM students")
results = cursor.fetchall()

# Print results
for row in results:
    print(row)

# Close the connection
connection.close()
