# 🛠 Troubleshooting – Lab 36

## Issue 1: KeyError when accessing graph
**Cause:** Node missing from adjacency list  
**Fix:**  
Ensure every node exists as a key in the graph dictionary

---

## Issue 2: Infinite recursion in DFS
**Cause:** Missing visited set  
**Fix:**  
Always track visited nodes to avoid loops

---

## Issue 3: Output order differs
**Cause:** Graph structure or traversal order  
**Fix:**  
Traversal order depends on adjacency list ordering

---

## Issue 4: collections module error
**Cause:** Python version issue  
**Fix:**  
Use Python 3.x (collections is built-in)
