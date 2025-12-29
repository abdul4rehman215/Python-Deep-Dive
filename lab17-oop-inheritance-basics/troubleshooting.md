# 🛠 Troubleshooting – Lab 17

### Issue: Attribute not found in subclass
**Cause:** Parent constructor not called  
**Fix:** Use super().__init__() in the child class

---

### Issue: Parent method not executed
**Cause:** Method overridden without calling super()  
**Fix:** Call parent method inside overridden method

---

### Issue: Incorrect inheritance syntax
**Cause:** Missing parent class in definition  
**Fix:** Use class ChildClass(ParentClass):
