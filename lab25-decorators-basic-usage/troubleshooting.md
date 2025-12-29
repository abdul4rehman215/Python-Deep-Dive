# 🛠 Troubleshooting – Lab 25

## Issue 1: Decorator not executing
**Cause:** Decorator not applied using `@` syntax.  
**Fix:** Ensure `@decorator_name` is placed above the function.

---

## Issue 2: Function arguments not working
**Cause:** Wrapper function does not accept parameters.  
**Fix:** Use `*args` and `**kwargs` in the wrapper.

---

## Issue 3: Unexpected return value
**Cause:** Wrapper does not return the original function’s result.  
**Fix:** Store and return the result from the wrapped function.

---

## Issue 4: Confusing decorator flow
**Cause:** Nested functions not clearly structured.  
**Fix:** Add clear naming and comments for readability.
