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

## 2. Why Do We Need Closures?

`Closures are useful when:`

- You want to keep data hidden (encapsulation without classes).

- You want to create function factories (functions that generate other functions).

- You want to avoid using global variables but still maintain state.

## 3. Requirements for Closures

`For something to be called a closure:`

- Must have a nested function.

- The nested function must refer to a variable from the enclosing scope.

- The outer function must return the nested function.