# 🛠 Troubleshooting – Lab 29

## Issue 1: Table already exists error
**Cause:** Script rerun with persistent database.  
**Fix:** Use `DROP TABLE IF EXISTS` or recreate the database.

---

## Issue 2: Data not appearing in query
**Cause:** Missing `connection.commit()`.  
**Fix:** Always commit after insert operations.

---

## Issue 3: sqlite3 module not found
**Cause:** Python installation issue.  
**Fix:** Reinstall Python or verify standard library availability.

---

## Issue 4: Database file not created
**Cause:** Using `:memory:` database.  
**Fix:** Use a file path (e.g., `sqlite3.connect("data.db")`) to persist data.
