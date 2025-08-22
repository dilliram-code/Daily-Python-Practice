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
---
## 2. Types of Namespaces in Python

Python has different levels of namespaces:
`1.✅Built-in Namespace`

- Contains all built-in functions and exceptions.
- Example: print(), len(), Exception, etc.
- Always available.
```python
print(len([1, 2, 3]))   # Both print and len come from built-in namespace

```
`2.✅Global Namespace`

- Created when a Python file (module/script) is run.
- Contains variables, functions, and classes defined at the top-level of the file.
```python
x = 100   # global namespace variable

def show():
    print(x)  # accessing global variable
show()

```
`3.✅Local Namespace`

- Created when a function is called.
- Contains names defined inside the function (parameters, local variables).
```python
def demo():
    a = 50  # local namespace
    print("Local:", a)

demo()
# print(a)  # ❌ Error: 'a' not defined globally

```
`4.✅Enclosing Namespace (nonlocal)`

- Exists when you have nested functions.
- Inner function can access variables from the outer function’s scope (using nonlocal if you want to modify).
```python
def outer():
    x = "outer"

    def inner():
        print("Enclosing:", x)  # x from outer scope
    inner()

outer()

```
---

