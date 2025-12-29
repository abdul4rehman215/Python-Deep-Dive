# 🛠 Troubleshooting – Lab 23

## Issue 1: Regex not matching expected text
**Cause:** Incorrect pattern or missing escape characters.  
**Fix:** Verify regex syntax and test using small strings.

---

## Issue 2: Unexpected empty match list
**Cause:** Pattern does not exist in the target string.  
**Fix:** Confirm the input string contains matching text.

---

## Issue 3: Confusing escape sequences
**Cause:** Not using raw strings.  
**Fix:** Prefix regex patterns with `r""`.

---

## Issue 4: RecursionError or performance issues
**Cause:** Overly complex or greedy patterns.  
**Fix:** Simplify regex and avoid unnecessary backtracking.
