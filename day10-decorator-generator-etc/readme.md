## ✅1. What is a decorator?

- A decorator is a function that takes another function as input and extends or modifies its behavior without changing the original function's code.

- Used for logging, authentication, performance measurement, caching, etc.

## ✅2. What is a generator?

- A generator is a lazy iterator that produces items on demand using yield. It avoids storing all values in memory.
***Advantages:***

- Memory efficient (generates values on the fly)

- Can represent infinite sequences

## ✅3. Understanding the Difference Between `a, b = b, a + b` and `a = b; b = a + b`

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

## ✅4. Using `_` in Python Loops and Assignments

In Python, the underscore `_` is often used as a **throwaway variable** — meaning the value exists but we don’t care about it.  

It’s a convention to say:  
👉 *“I know there’s a value here, but I don’t need it.”*  

---

## 🔹 Example 1: Repeat something `N` times  

```python
for _ in range(5):
    print("Hello")

    # output:
    Hello
    Hello
    Hello
    Hello
    Hello
```
## 🔹 Example 2: Ignoring multiple values in unpacking
```python
a, _, c = (1, 2, 3)
print(a, c)
```
The middle value 2 is ignored using _.

## **✅ Summary**

- _ is used in loops or unpacking when the value is not important.
- It improves readability and clearly shows intent.