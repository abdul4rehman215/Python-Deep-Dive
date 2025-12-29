# 🛠 Troubleshooting – Lab 15

### Issue: python3 -m venv fails
**Cause:** venv module not installed  
**Fix:** Install python3-venv package

---

### Issue: pip installs globally instead of venv
**Cause:** Virtual environment not activated  
**Fix:** Run source myenv/bin/activate

---

### Issue: Permission denied during pip install
**Cause:** Incorrect Python/pip path  
**Fix:** Ensure pip belongs to the active virtual environment
