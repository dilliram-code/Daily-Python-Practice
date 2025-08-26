`1) What is Recursion?`

- Recursion is when a function calls itself to solve a problem by breaking it into smaller subproblems of the same form.

`Every recursive function has:`

- Base case(s): the smallest input(s) you can answer directly.

- Recursive case: a step that reduces the problem size and calls itself.

`2) How Calls Work: The Call Stack`

- Each function call gets its own stack frame (arguments, local variables, return address). Frames form a stack (LIFO). If recursion goes too deep without stopping, you’ll hit:
```python
RecursionError: maximum recursion depth exceeded
```
### 🚩 Drawbacks of Using Recursion in Python
`1. High Memory Usage (Stack Overflow Risk)`

- Each recursive call adds a new frame to the call stack. Too many calls can cause a stack overflow error.

- Example: Factorial Function (deep recursion)
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# This will cause RecursionError
print(factorial(2000))

```
`🔴 Error:`
```python
RecursionError: maximum recursion depth exceeded in comparison
```
`👉 By default, Python’s recursion depth is limited (~1000).`


`✅ Summary`

- Stack Overflow (RecursionError for deep recursion).

- Slower execution due to function call overhead.

- Harder to debug and trace compared to iteration.

- Memory inefficiency with immutable objects (like list slicing).

- Not beginner-friendly in many cases.

`👉 Rule of thumb:`

- Use recursion for problems with natural recursive structure (tree traversals, divide-and-conquer).

- Use loops for simple repetitive tasks (factorial, Fibonacci, summation).