# 🛠 Troubleshooting – Lab 37

## Issue 1: TypeError when using *args
**Cause:** Passing non-numeric values to summation  
**Fix:**  
Ensure only numeric values are passed

---

## Issue 2: KeyError in **kwargs
**Cause:** Accessing keys directly without checking  
**Fix:**  
Iterate using kwargs.items()

---

## Issue 3: Function receives empty args
**Cause:** No arguments passed  
**Fix:**  
Validate input before processing

---

## Issue 4: Unpacking error
**Cause:** Forgetting * or ** during unpacking  
**Fix:**  
Use * for lists and ** for dictionaries
