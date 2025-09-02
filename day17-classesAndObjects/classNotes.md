**1 — What is a class and an object?**

- `Class`: a blueprint or template that defines attributes (data) and methods (behavior).

- `Object (instance)`: a concrete occurrence of a class — it holds actual data.

**2 — self: what it is and why it matters**

- `self` is the convention for the first parameter of instance methods. It refers to the instance on which the method is called.

Key points:

- `self` is just a name — you could use `this` or `me`, but `self` is the universal convention.

- Methods are functions that expect the instance as their first argument. When you call `obj.method(args...)`, Python implicitly passes obj as the first argument.
```python
class Counter:
    def __init__(self, start=0):
        self.count = start  # store on the instance

    def increment(self, n=1):
        self.count += n

c = Counter(10)
c.increment(2)        # behind the scenes: Counter.increment(c, 2)
print(c.count)        # 12
```

**3 — What is __init__?**

- `__init__` is a special method in Python classes.

- It’s called automatically when you create (instantiate) an object.

- It’s often referred to as the constructor of the class (though technically in Python, object creation happens in `__new__`, but `__init__` initializes it).

- 👉 Think of `__init__` as the setup function that prepares an object with initial values.

**4. `__new__` vs `__init__` in Python**

Role of `__new__`

- `__new__` is a class method (technically a static method defined on the class) responsible for creating a new instance of a class.

- It is called before `__init__`.

- It always returns a new instance of the class (or another object).

Syntax:
```python
def __new__(cls, *args, **kwargs):
    # create and return new instance
```

Role of `__init__`

- `__init__` is an initializer (not a constructor in strict sense).

- It initializes the instance returned by `__new__`.

- It does not return anything (must return None).

Syntax:
```python
def __init__(self, *args, **kwargs):
    # initialize attributes
```
**The Flow**

When you do:
```python
obj = MyClass(10)
```
Internally:

- `MyClass.__new__(MyClass, 10)` → creates instance.

- The new instance is passed to `MyClass.__init__(obj, 10)` → initializes attributes.

Finally, `obj` is returned.

**Basic Example**
```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Inside __new__ (creating instance)")
        instance = super().__new__(cls)  # actually create object
        return instance

    def __init__(self, value):
        print("Inside __init__ (initializing instance)")
        self.value = value

obj = MyClass(5)
print(obj.value)
```
output:
```python
Inside __new__ (creating instance)
Inside __init__ (initializing instance)
5
```