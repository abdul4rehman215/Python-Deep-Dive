# 🛠 Troubleshooting – Lab 27

## Issue 1: Threads not running concurrently
**Cause:** Threads not started properly.  
**Fix:** Ensure `start()` is called, not the function directly.

---

## Issue 2: Program exits before threads finish
**Cause:** Missing `join()` calls.  
**Fix:** Use `join()` to wait for thread completion.

---

## Issue 3: Output order is inconsistent
**Cause:** Normal thread scheduling behavior.  
**Fix:** This is expected; do not rely on output order.

---

## Issue 4: Data inconsistency in shared variables
**Cause:** Race conditions due to shared memory.  
**Fix:** Use locks or synchronization mechanisms when needed.
