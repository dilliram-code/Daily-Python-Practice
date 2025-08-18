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