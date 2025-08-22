## 1. What is a Namespace?

A namespace is simply a mapping between names (identifiers) and the objects they refer to.

Think of it as a dictionary where keys = names, and values = objects.

`👉 Example:`
```python
x = 10
y = "Hello"

```
Here:

- Name `x` refers to object  `10`.
- Name `y` refers to object `"Hello"`.

Internally, Python stores them in a namespace like:
```python
{
    'x': 10,
    'y': "Hello"
}

```
***So, a namespace ensures that names are unique and do not conflict with each other.***