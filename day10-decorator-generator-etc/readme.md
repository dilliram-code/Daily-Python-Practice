## ✅1. What is a decorator?

- A decorator is a function that takes another function as input and extends or modifies its behavior without changing the original function's code.

- Used for logging, authentication, performance measurement, caching, etc.

## ✅2. What is a generator?

- A generator is a lazy iterator that produces items on demand using yield. It avoids storing all values in memory.
***Advantages:***

- Memory efficient (generates values on the fly)

- Can represent infinite sequences

## ✅2. Understanding the Difference Between `a, b = b, a + b` and `a = b; b = a + b`

## 📌 Introduction
In Python, assignment works differently depending on whether **tuple unpacking** (multiple assignment) is used or not.  
This document explains the subtle difference between:

```python
a, b = b, a + b
```
and 
```python
a = b
b = a + b
```
## 🔹 Case 1: Tuple Assignment in Fibonacci

In Python, you can update multiple variables at once using **tuple unpacking**.

### How it works:
- Both right-hand side expressions are **evaluated first**.
- Then, values are **assigned simultaneously** to `a` and `b`.
- This avoids overwriting issues.

---

### Example:
```python
a, b = 1, 2
a, b = b, a + b
print(a, b)

# output: 2 3
```
✔ Explanation:
a = b → a = 2
b = a + b → b = 2 + 2 = 4

## 🔹 Case 2: Sequential Assignment in Fibonacci

In this method, assignments happen **one after another** (sequentially).  

### How it works:
- First line updates `a`.
- Second line uses the **new value of `a`**, not the old one.
- This can lead to different results compared to tuple assignment.

---

### Example:
```python
a, b = 1, 2
a = b
b = a + b
print(a, b)

# Output: 2 4
```
✔ Explanation:
a = b → a = 2
b = a + b → b = 2 + 2 = 4