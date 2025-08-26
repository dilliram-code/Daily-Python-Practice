### What is a function?

A function is a named block of reusable code that:

- Can accept inputs (arguments),

- Optionally produce an output (return value),

- Encapsulates logic so you can reuse/compose it.

`Note:`In Python functions are first-class objects — you can assign them, pass them, return them.

Defining & calling functions
```python
def greet(name: str) -> str:
    """Return a greeting for name."""
    return f"Hello, {name}!"

print(greet("Aarav"))  # Hello, Aarav!
```

- `def` creates the function object and binds it to the name greet.

- The body runs only when the function is called.

- `-> str` is a return annotation (optional); not enforced at runtime.