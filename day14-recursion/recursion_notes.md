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