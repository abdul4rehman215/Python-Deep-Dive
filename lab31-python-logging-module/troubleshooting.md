# 🛠 Troubleshooting – Lab 31

## Issue 1: Logs not appearing
**Cause:** Logging level too high.  
**Fix:** Set level=logging.DEBUG or INFO.

---

## Issue 2: Duplicate log messages
**Cause:** Multiple logging configurations.  
**Fix:** Configure logging only once.

---

## Issue 3: Logs hard to read
**Cause:** Missing format configuration.  
**Fix:** Add format string in basicConfig().

---

## Issue 4: Application crashes on error
**Cause:** Exception not handled.  
**Fix:** Wrap risky logic in try/except and log errors.
