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