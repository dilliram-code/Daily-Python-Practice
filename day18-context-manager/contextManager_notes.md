**🌟 1. What is a Context Manager?**

- A Context Manager is a construct in Python that allows you to allocate and release resources automatically.
It is mostly used with the `with` statement.

`👉 Example (most common):`
```python
with open("example.txt", "w") as f:
    f.write("Hello, Context Manager!")
```
Here:

- `open("example.txt", "w")` → acquires the resource (opens the file).
- `f.write(...)` → uses the resource.
- When the block ends, Python automatically closes the file, even if an exception occurs.

Without context manager, you’d need:
```python
f = open("example.txt", "w")
try:
    f.write("Hello, Context Manager!")
finally:
    f.close()  # must close manually
```
`💡 So, context managers = simplify resource handling (files, DB connections, sockets, locks, etc.).`