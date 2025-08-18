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
