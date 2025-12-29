# 🛠 Troubleshooting – Lab 14

### Issue: pdb prompt not appearing
**Cause:** Script exited before breakpoint  
**Fix:** Ensure `pdb.set_trace()` is executed

---

### Issue: Program crashes before debugging
**Cause:** No exception handling  
**Fix:** Combine pdb with try-except if needed

---

### Issue: Too many print statements
**Cause:** Excessive debug output  
**Fix:** Remove print debugging after issue is fixed
