# 🛠 Troubleshooting – Lab 34

## Issue 1: matplotlib not installed
**Error:** ModuleNotFoundError  
**Fix:**  
Run `pip3 install matplotlib`

---

## Issue 2: Plot window does not appear
**Cause:** Running in a headless/cloud environment  
**Fix:**  
This is expected. The script still executes correctly.

---

## Issue 3: Script exits without output
**Cause:** plt.show() missing  
**Fix:**  
Ensure plt.show() is included at the end of the script.

---

## Issue 4: Permission errors during install
**Cause:** System-level Python restrictions  
**Fix:**  
Use `pip3 install --user matplotlib`
