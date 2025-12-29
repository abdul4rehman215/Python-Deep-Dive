# 🛠 Troubleshooting – Lab 35

## Issue 1: ModuleNotFoundError for collections
**Cause:** Python version is too old  
**Fix:**  
Use Python 3.x (collections is built-in)

---

## Issue 2: Script runs but no output
**Cause:** print statements missing  
**Fix:**  
Ensure print() calls are present

---

## Issue 3: Incorrect order of output
**Cause:** deque operations misunderstood  
**Fix:**  
Verify whether append/pop or appendleft/popleft is used

---

## Issue 4: Counter output order confusion
**Cause:** Dictionary ordering vs frequency  
**Fix:**  
Use most_common() for sorted frequency results
