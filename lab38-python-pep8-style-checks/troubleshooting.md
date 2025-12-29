# 🛠 Troubleshooting – Lab 38

## Issue 1: flake8 command not found
**Cause:** Tool not installed  
**Fix:**  
Run `pip install flake8`

---

## Issue 2: black reformats code unexpectedly
**Cause:** Black enforces strict style  
**Fix:**  
This is expected behavior

---

## Issue 3: autopep8 not fixing all issues
**Cause:** Limited aggression level  
**Fix:**  
Use `--aggressive` flags

---

## Issue 4: Permission denied during installation
**Cause:** System Python restrictions  
**Fix:**  
Use `pip install --user flake8 black autopep8`
