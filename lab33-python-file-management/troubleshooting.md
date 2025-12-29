# 🛠 Troubleshooting – Lab 33

## Issue 1: Script fails with FileNotFoundError
**Cause:** Source directory does not exist.  
**Fix:** Ensure `source_folder` is created before running the script.

---

## Issue 2: Files not copied
**Cause:** Incorrect file paths.  
**Fix:** Use os.path.join() instead of hardcoding paths.

---

## Issue 3: Permission denied error
**Cause:** Insufficient permissions.  
**Fix:** Run the script in a writable directory.

---

## Issue 4: Duplicate files created
**Cause:** Script run multiple times.  
**Fix:** Clear destination folder before rerunning or add overwrite logic.
