## 1. Introduction

- A closure in Python is a function object that remembers values in the enclosing scopes even if the scope is no longer available.
`In other words:`
- 👉 A closure is a function defined inside another function that captures variables from the outer function.
```python
def outer_function():
  message = "Hello"
  def inner_function():
    print(message)
  return inner_function

my_func = outer_function()
my_func()

# Output: Hello
```
- ✅ Even though outer_function has finished execution, inner_function still remembers message. This is what makes it a closure.