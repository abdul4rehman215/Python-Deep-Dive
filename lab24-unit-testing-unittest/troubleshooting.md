# 🛠 Troubleshooting – Lab 24

## Issue 1: Tests not discovered
**Cause:** Test file or method naming is incorrect.  
**Fix:** Ensure filenames start with `test_` and methods start with `test_`.

---

## Issue 2: Assertion failure
**Cause:** Function logic does not match expected output.  
**Fix:** Re-check function implementation and expected values.

---

## Issue 3: ImportError during test run
**Cause:** Missing imports or incorrect module paths.  
**Fix:** Verify import statements and file locations.

---

## Issue 4: unittest.main() not executing
**Cause:** Missing `if __name__ == "__main__":` block.  
**Fix:** Add the correct test runner boilerplate.
