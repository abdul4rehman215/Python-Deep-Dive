# 🛠 Troubleshooting – Lab 12

### Issue: Program crashes without message
**Cause:** Missing exception handling  
**Fix:** Wrap risky code inside try-except blocks

---

### Issue: ZeroDivisionError
**Cause:** User entered 0  
**Fix:** Add a specific except ZeroDivisionError block

---

### Issue: Invalid input causes crash
**Cause:** input() returns string  
**Fix:** Catch ValueError during type conversion
