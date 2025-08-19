## 1. Why Exception Handling Exists

In programming, sometimes unexpected events occur during code execution, such as:

- Dividing by zero  
- Accessing a file that doesn’t exist  
- Converting a string to a number incorrectly  

Without exception handling, Python stops execution and raises an error.  

### Example

```python
x = 5
y = 0
print(x / y)  # ZeroDivisionError
```
Output:
```python 
ZeroDivisionError: division by zero
```
This stops the program.

- `✅ Solution:` Exception handling allows you to gracefully handle errors, keep the program running, and take appropriate actions instead of crashing.
---

## 2. Common Built-in Exceptions

| **Exception**       | **Cause**                                        |
|---------------------|--------------------------------------------------|
| `ZeroDivisionError` | Division by zero                                 |
| `ValueError`        | Invalid type conversion (e.g., `int("abc")`)     |
| `TypeError`         | Operation on incompatible types                  |
| `FileNotFoundError` | File not found                                   |
| `IndexError`        | List index out of range                          |
| `KeyError`          | Dictionary key not found                         |
| `AttributeError`    | Accessing a non-existing attribute               |
| `ImportError`       | Module or object cannot be imported              |
| `NameError`         | Variable not defined                             |
| `OSError`           | OS-related errors (e.g., file access issues)     |

