### 🔹 1. Type Casting (Explicit Conversion)

**What it is:**  
When you, the programmer, manually convert a value from one type to another.

**How to do it:**  
Uses built-in functions like `int()`, `float()`, `str()`, `list()`, etc.

**Example:**
```python
# Explicit type casting
x = "10"
y = int(x)   # convert string "10" to integer 10
print(y + 5)   # Output: 15
```

### 🔹 2. Type Coercion (Implicit Conversion)

**What it is:**  
When Python automatically converts a value from one type to another during an operation to avoid errors or data loss.

**When it happens:**  
Usually occurs in expressions with mixed data types.

**Example:**
```python
# Implicit type coercion
x = 10       # int
y = 3.5      # float
z = x + y    # Python converts int -> float automatically
print(z)     # Output: 13.5
```

**✅ Key Difference:**
- Casting = You force it.
- Coercion = Python forces it.
---

### 🔹 Weird Behavior of Division in Python

Division in Python can be confusing because it behaves differently in Python 2 and Python 3, and there are two operators: `/` and `//`.

#### 🔹 1. True Division (`/`)

- Always returns a **float**, even if both operands are integers.

**Example:**
```python
print(5 / 2)   # Output: 2.5
print(4 / 2)   # Output: 2.0  (float, not int)
```
***⚠️ Weirdness:***
- Even when it looks like the answer should be an integer, Python keeps it as float (2.0 instead of 2).

#### 🔹 2. Floor Division (`//`)

- Returns the **floor value** (rounded down) of the division.  
- Works for both integers and floats.

**Example:**
```python
print(5 // 2)     # Output: 2
print(5.0 // 2)   # Output: 2.0
```
***⚠️ Weirdness with Negatives:***
- Floor division rounds towards negative infinity, not towards zero.
```python
print(5 // 2)     # Output: 2
print(-5 // 2)    # Output: -3   (not -2!)
```

### 🔹 3. Modulo with Negative Numbers

- Modulo in Python follows **floor division rules**, which can sometimes be confusing.

**Example:**
```python
print(5 % 2)     # Output: 1
print(-5 % 2)    # Output: 1    (not -1, because result has same sign as divisor)
print(5 % -2)    # Output: -1
print(-5 % -2)   # Output: -1
```
***👉 Rule:***
- a % b always has the same sign as b (the divisor).

### ✅ Summary

- **Casting** → Explicit conversion by the user using functions like `int()`, `float()`, `str()`, etc.  
- **Coercion** → Automatic conversion by Python (e.g., `int → float` in mixed operations).  

**Division Rules:**
- `/` → **True Division** → always returns a `float`.  
- `//` → **Floor Division** → rounds **down** (towards negative infinity, not zero).  

**Important Notes:**
- Negative floor division behaves differently:  
  `-5 // 2 = -3` (not `-2`).  
- Modulo (`%`) follows the divisor’s sign:  
  `-5 % 2 = 1`, `5 % -2 = -1`.  
- Division by zero → **Error** (Python does not return Infinity).  
---

# 🐍 Objects in Python

In Python, **everything is an object**:  
Numbers, strings, functions, classes, and even instances are all objects.

An **object** bundles three key things:

---

## 🔹 1. Identity

- Each object has a unique identity during its lifetime.  
- You can check it with:
  ```python
  x = 42
  print(id(x))   # unique identifier (like memory address)

## 🔹 2. Type

- The type defines what kind of object it is and what it can do.
- Determines behavior (methods, operators).
```python
x = 42
print(type(x))   # <class 'int'>
```
## 🔹 3. State (Attributes)

- Represents the object’s data.
- Stored in attributes (obj.__dict__ for most user-defined objects).
```python
class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Buddy")
print(d.__dict__)   # {'name': 'Buddy'}
```
### ✅ Summary

- Identity → "Who" the object is (id).

- Type → "What" the object is (type).

- State → "What data" the object holds (attributes).

`📌 In short:`
- Objects in Python = Identity + Type + State

# 🔹 Normal Function vs Generator
## `1. Normal Function`

- A normal function in Python executes all its statements at once.
- It returns a value (using return) and terminates immediately.
- Each call creates a new function frame in memory, so intermediate states are lost.
- If you want a sequence of results, you must either return a list or call it repeatedly.

`👉 Example:`
```python
def normal_function(n):
    result = []
    for i in range(1, n+1):
        result.append(i*i)
    return result

print(normal_function(5))  
# Output: [1, 4, 9, 16, 25]

```
- Here, all squares are calculated at once and stored in memory before being returned.
- Memory heavy for large values of `n`.

## `2. Generator Function`

- A generator function looks like a normal function but uses yield instead of return.
- Instead of computing everything at once, it produces values one at a time when requested (lazy evaluation).
- Generators remember their state between calls (where they left off).
- They are memory-efficient because they don’t store the entire result in memory.

`👉 Example:`
```python
def generator_function(n):
    for i in range(1, n+1):
        yield i*i   # yield produces values one at a time

gen = generator_function(5)

print(next(gen))  # 1
print(next(gen))  # 4
print(next(gen))  # 9

# Or iterate fully
for val in generator_function(5):
    print(val)
# Output: 1, 4, 9, 16, 25

```
# 🔹 When to Use Which?

`✅ Use normal functions when:`

- Data size is small
- You need random access to results

`✅ Use generators when:`

- Data size is huge (big lists, streams, files, API data)
- You want memory efficiency and lazy evaluation

`👉 In short:`
- Normal function = "Cook all food at once and serve."
- Generator = "Serve food one plate at a time when asked."
---

## 🔹 return vs yield in Python
`1. return`

- Ends the function immediately.
- Sends back one value (or object) to the caller.
- Function cannot be resumed once it has returned.
```python 
def square_numbers(n):
    result = []
    for i in range(1, n+1):
        result.append(i * i)
    return result

print(square_numbers(5))
# output: [1, 4, 9, 16, 25]

```
- Here, the function builds the whole list in memory and returns it at once.
- After return, the function is done and cannot be resumed.

`2. yield`

- Turns a normal function into a generator.
- Does not end the function immediately.
- Saves the state of the function (local variables, position in loop).
- Allows resumption from where it left off.
- Produces values one at a time (lazy evaluation).
```python
def square_numbers_gen(n):
    for i in range(1, n+1):
        yield i * i   # yields one value at a time

gen = square_numbers_gen(5)

print(next(gen))  # 1
print(next(gen))  # 4
print(list(gen))  # [9, 16, 25] -> continues from where it left

```
- With yield, the function pauses at each value, remembers where it was, and continues next time.

## 🟢 What is __repr__ in Python? (deep dive)

- `__repr__` is a special method that returns the official string representation of an object. It’s what you see in the REPL, in debug logs, and when you call `repr(obj)` or format with `!r`. Its goal is to be unambiguous and, when reasonably possible, look like valid Python code that could recreate the object.


# 🔹random.randint() vs random.randrange()

`random.randint(a, b)`

- Returns an integer between a and b inclusive.

Example:
```python
import random
print(random.randint(1, 6))  # 1,2,3,4,5,6 possible
```
`random.randrange(start, stop, step=1)`
- Works like `range()`.
- Returns a random number from the sequence start to stop-1.
- stop is exclusive.
- You can also control steps.

Example:
```python
import random
print(random.randrange(1, 6))     
# 1,2,3,4,5 possible (6 not included)

print(random.randrange(0, 10, 2)) 
# 0,2,4,6,8 possible
```
`👉 Key difference:`

- `randint(a, b)` → both ends included.

- `randrange(start, stop)` → stop not included, behaves like range().

`Note`:
- Both `randint()` and `randrange()` cannot produce
float value number