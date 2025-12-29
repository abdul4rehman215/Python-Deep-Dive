# 🛠 Troubleshooting – Lab 22

## Issue 1: ModuleNotFoundError: No module named 'requests'
**Cause:** requests library is not installed.  
**Fix:** Run `pip install requests`.

---

## Issue 2: ConnectionError or Timeout
**Cause:** No internet connection or firewall restrictions.  
**Fix:** Verify network connectivity and retry.

---

## Issue 3: JSONDecodeError
**Cause:** Response body is not valid JSON.  
**Fix:** Check response headers and ensure API returns JSON.

---

## Issue 4: KeyError when accessing JSON fields
**Cause:** Incorrect or missing key.  
**Fix:** Use dictionary `.get()` method instead of direct indexing.
