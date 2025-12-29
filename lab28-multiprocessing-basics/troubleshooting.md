# 🛠 Troubleshooting – Lab 28

## Issue 1: Script runs infinitely
**Cause:** Missing `if __name__ == "__main__":` guard.  
**Fix:** Always wrap process creation inside the main guard.

---

## Issue 2: High memory usage
**Cause:** Large data passed to multiple processes.  
**Fix:** Optimize data size or use shared memory if required.

---

## Issue 3: Output order is inconsistent
**Cause:** Normal multiprocessing scheduling behavior.  
**Fix:** Do not rely on output order.

---

## Issue 4: Slower execution than expected
**Cause:** Process startup overhead.  
**Fix:** Use multiprocessing only for CPU-intensive workloads.
