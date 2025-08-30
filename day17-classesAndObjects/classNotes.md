**1 — What is a class and an object?**

- `Class`: a blueprint or template that defines attributes (data) and methods (behavior).

- `Object (instance)`: a concrete occurrence of a class — it holds actual data.

**2 — self: what it is and why it matters**

- `self` is the convention for the first parameter of instance methods. It refers to the instance on which the method is called.

Key points:

- `self` is just a name — you could use `this` or `me`, but `self` is the universal convention.

- Methods are functions that expect the instance as their first argument. When you call `obj.method(args...)`, Python implicitly passes obj as the first argument.