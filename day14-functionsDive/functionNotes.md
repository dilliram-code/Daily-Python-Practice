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
Here:

- The function square() is applied to each element of numbers.

**2. filter() Function**

✅ Syntax:
```python
filter(function, iterable)
```
- function → Must return True or False.

- iterable → Items will be passed to the function, and only those returning True remain.

It returns a filter object (an iterator).

`🟢 Basic Example:`
```python
numbers = [1, 2, 3, 4, 5, 6]

def is_even(x):
    return x % 2 == 0

result = filter(is_even, numbers)
print(list(result))   # [2, 4, 6]

```

**3. reduce() Function**

- Unlike map and filter, reduce() is not built-in in Python 3.
- You must import it:
```python
from functools import reduce
```
✅ Syntax:
```python
reduce(function, iterable[, initializer])
```
- function → A function that takes two arguments.

- iterable → Sequence to process.

- initializer → Optional starting value.

It applies the function cumulatively, reducing the iterable to a single value.

`🟢 Basic Example:`
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

def add(x, y):
    return x + y

result = reduce(add, numbers)
print(result)   

# 15
```
Here:

- (((1+2)+3)+4)+5 = 15

`When to Use?`

- Use map when you want to transform each element.
- Use filter when you want to select elements based on a condition.
- Use reduce when you want to combine elements into a single result.

**🟩What is zip()?**

- The built-in `zip()` function is used to combine two or more iterables (like lists, tuples, strings, etc.) into a single iterable of tuples, where each tuple contains one element from each iterable.

`👉 Think of a zipper joining two chains together → that’s how zip() works.`
```python
zip(iterable1, iterable2, ...)
```
Basic Example:
```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

zipped = zip(names, scores)   # returns a zip object
print(list(zipped))  
# Output: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
```
`🔑 Each tuple pairs the elements from the same index.`

**🟩 What is enumerate()?**

- The built-in enumerate() function is used when you want both the index and the value while looping over an iterable.
```python
enumerate(iterable, start=0)
```
- iterable: list, tuple, string, etc.
- start: index to begin from (default is 0).

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry
```
`Key Takeaways:`
- ✅ zip() → Combine multiple iterables element-wise.
- ✅ enumerate() → Loop with index and value together.

**🟩 What is a Lambda Function?**

- A lambda function is a small, anonymous function in Python.

- Anonymous means it doesn’t need a name (like `def`).

- It can take any number of arguments but can only contain one expression.

`✅ Syntax:`
```python
lambda arguments: expression
```
- lambda → keyword.
- arguments → input parameters (like in normal functions).
- expression → a single expression whose result is automatically returned.

`🟢 Basic Example:`
```python
square = lambda x: x ** 2
print(square(5))   

# 25
```
equivalent to:
```python
def square(x):
    return x ** 2
```