# 🛠 Troubleshooting – Lab 21

## Issue 1: FileNotFoundError
**Cause:** CSV file does not exist in the directory.  
**Fix:** Ensure sample.csv is in the same folder as the script.

---

## Issue 2: CSV rows printed as strings only
**Cause:** csv module reads all values as strings by default.  
**Fix:** Convert values manually using int() or float() when required.

---

## Issue 3: Header included unexpectedly
**Cause:** Header row not skipped.  
**Fix:** Use next(csv_reader) before looping.

---

## Issue 4: KeyError when accessing dictionary
**Cause:** Incorrect column name used.  
**Fix:** Match key names exactly as defined in CSV headers.
