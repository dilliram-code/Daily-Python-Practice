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



## 🎯 Interview Q&A on Python Closures
`Q1. Why do we use closures instead of global variables?`

- Closures allow state preservation without polluting the global scope. They are safer and prevent naming conflicts.

`Q2. What are the requirements for a closure?`

- Nested function.

- Inner function refers to outer scope variable.

- Outer function returns inner function.

`Q3. How do closures relate to decorators?`

- Decorators in Python are built on closures. A decorator is essentially a closure that takes a function and returns a modified function.

`Q4. What is the late binding problem in closures?`

- Closures capture variables, not values. If the variable changes later, all closures referencing it will see the updated value.
`✅ Fix: use default arguments (def f(x=x):).`

`Q5. How to check if a function is a closure?`

- Check __closure__ attribute. If not None, the function has closed-over variables.

`Q6. Compare closures with classes.`

- Closures can encapsulate state like objects, but classes are more structured and support inheritance. Closures are lighter when only data hiding and function factory behavior is needed.


### 🔹 Interview QnA on Closures and State Tracking

`Q1: What is a closure in Python?`
- A closure is a function object that has access to variables from its enclosing scope, even after that scope has finished execution.

`Q2: Why are closures useful for state tracking?`
- They allow you to maintain state across function calls without using global variables or class instances.

`Q3: What role does nonlocal play in closures?`
- nonlocal allows you to modify a variable from the nearest enclosing (non-global) scope inside a nested function.

`Q4: Give a real-world use case of closures.`
- Implementing counters, caching, decorators, login attempt tracking, or API rate limiting.

`Q5: How is closure-based state tracking different from using classes?`
- Closures are functional and encapsulate state via nested functions, while classes encapsulate state via attributes. Closures are often more lightweight and useful for small, functional-style stateful logic.