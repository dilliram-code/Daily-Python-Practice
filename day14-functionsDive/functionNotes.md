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

Parameters & arguments (all forms)

- Python supports many parameter styles. Understand these well.

`1. Positional and keyword arguments`
```python
def f(a, b, c=3):
    return a + b + c

f(1, 2)         # positional: a=1, b=2, c=3
f(1, b=2, c=5)  # mix of positional and keywords

```

`2.Var positional (*args) and var keyword (**kwargs)`

```python
def f(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

f(1, 2, a=3, b=4)
# args: (1, 2)
# kwargs: {'a': 3, 'b': 4}

```

## 🚀 Python map(), filter(), and reduce() — Complete Guide
These three functions are functional programming tools in Python. They help process collections (like lists, tuples, sets) without writing explicit `for` loops.

- They use iterators under the hood, which means they are memory efficient and can handle large data streams.

**1. map() Function**

✅ Syntax:
```python
map(function, iterable)
```
- function → A function that will be applied to each item in the iterable.

- iterable → Any iterable (list, tuple, set, etc.).

It returns a map object (an iterator), which can be converted to a list, tuple, etc.

`🟢 Basic Example:`
```python
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

result = map(square, numbers)
print(list(result))   

# [1, 4, 9, 16, 25]
```