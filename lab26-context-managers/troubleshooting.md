# 🛠 Troubleshooting – Lab 26

## Issue 1: __enter__ or __exit__ not executing
**Cause:** Context manager not used with `with`.  
**Fix:** Always use the `with` statement.

---

## Issue 2: File not closing properly
**Cause:** Missing close logic in `__exit__`.  
**Fix:** Ensure `self.file.close()` is called.

---

## Issue 3: Exception stops program
**Cause:** Exception not handled properly.  
**Fix:** Use `__exit__()` to manage cleanup safely.

---

## Issue 4: Confusing execution flow
**Cause:** Lack of print/debug statements.  
**Fix:** Add logging or print statements for clarity.
