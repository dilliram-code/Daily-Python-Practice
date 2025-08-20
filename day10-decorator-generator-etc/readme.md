## ✅1. What is a decorator?

- A decorator is a function that takes another function as input and extends or modifies its behavior without changing the original function's code.

- Used for logging, authentication, performance measurement, caching, etc.

## ✅2. What is a generator?

- A generator is a lazy iterator that produces items on demand using yield. It avoids storing all values in memory.
***Advantages:***

- Memory efficient (generates values on the fly)
- Can represent infinite sequences

## What is an Iteration?
- Iteration is a general term for takig each item of something, one after another. Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration.
```python
num = [1,2,3]

for i in num:
  print(i)

# output:
1
2
3
```


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

## ✅5. What is an Iterator?
An **iterator** is an object that implements:
- `__iter__()` → returns the iterator object itself.
- `__next__()` → returns the next value from the sequence.  
  When no items are left, it raises a `StopIteration` exception.

  **More explanation on Iterator**
- An iterator in Python is an object that contains a countable number of elements that can be iterated upon. In simpler words, we can say that Iterators are objects that allow you to traverse through all the elements of a collection and return one element at a time. More specifically, we say that an iterator is an object that implements the iterator protocol.

- Lists, tuples, dictionaries, strings and sets are all iterable objects. They are iterable containers that you can convert into an iterator.

**‼Note:**
- Note that every iterator is also an iterable, but not every iterable is an iterator. For example, a tuple is iterable, but it is not an iterator. An iterator can be created from an iterable by using the function iter(). Thus, when we pass this tuple to an iter() function, we will get an iterator.