**1 — What is a class and an object?**

- `Class`: a blueprint or template that defines attributes (data) and methods (behavior).

- `Object (instance)`: a concrete occurrence of a class — it holds actual data.

**2 — self: what it is and why it matters**

- `self` is the convention for the first parameter of instance methods. It refers to the instance on which the method is called.

Key points:

- `self` is just a name — you could use `this` or `me`, but `self` is the universal convention.

- Methods are functions that expect the instance as their first argument. When you call `obj.method(args...)`, Python implicitly passes obj as the first argument.

**3 — What is __init__?**

- `__init__` is a special method in Python classes.

- It’s called automatically when you create (instantiate) an object.

- It’s often referred to as the constructor of the class (though technically in Python, object creation happens in `__new__`, but `__init__` initializes it).

- 👉 Think of `__init__` as the setup function that prepares an object with initial values.