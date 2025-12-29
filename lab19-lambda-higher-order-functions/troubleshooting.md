# 🛠 Troubleshooting – Lab 19

### Issue: reduce() not found
**Cause:** functools module not imported  
**Fix:** Add `from functools import reduce`

---

### Issue: map or filter returns unexpected output
**Cause:** Lambda logic incorrect  
**Fix:** Test lambda separately before using

---

### Issue: Code becomes hard to read
**Cause:** Overusing lambda functions  
**Fix:** Use normal function definitions for complex logic
