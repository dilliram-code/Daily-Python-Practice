**Magic Methods (Dunder Methods)**
- Magic methods (aka dunder methods) are special methods whose names start and end with double underscores, e.g. `__init__`, `__repr__`, `__add__`. Python calls them implicitly to implement language features (construction, arithmetic, iteration, attribute access, etc.). Implementing them lets your objects behave like `built-in` types.

**Common magic methods & what they do**
Object lifecycle / creation

- `__new__(cls, ...)` — low-level instance creation (returns instance)

- `__init__(self, ...)` — instance initialization

- `__del__(self)` — destructor (rarely used)

Representation

- `__repr__(self)` — developer representation (should be unambiguous)

- `__str__(self)` — human readable

Attribute access

- `__getattr__(self, name)` — called when attribute not found

- `__getattribute__(self, name)` — called for every attribute lookup

- `__setattr__(self, name, value)` — called on attribute assignment

- `__delattr__(self, name)` — called on del obj.attr

Descriptors

- `__get__(self, obj, cls)`, `__set__(self, obj, value)`, `__delete__(self, obj)`

- `__set_name__(self, owner, name)` — Python 3.6+ to learn attribute name

Callable / containers

- `__len__`, `__contains__`, `__iter__`, `__next__`, `__getitem__`, `__setitem__`, `__delitem__`

Context managers

- `__enter__`, `__exit__`

Numeric & operator overloading

- `__add__`, `__radd__`, `__iadd__`, `__mul__`, `__rmul__`, `__neg__`, etc.

Comparisons / hashing

- `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__hash__`

Other

- `__call__` (make instances callable)

- `__copy__` / `__deepcopy__` or implement via copy protocol

- `__getstate__` / `__setstate__` (pickling hooks)

**How Python looks up magic methods (important detail)**

- For many operations (like x + y) Python looks up special methods on the type (class), not the instance `x.__dict__`. That’s why adding `__add__` to an instance won't change behavior of `+`; you must define it on the class.

- Example: int.`__add__` is used for `1 + 2`.

`Implementation note:`

 If you implement `__add__` on a class, Python will call it for a + b. If it returns NotImplemented, Python will try the reflected method (`__radd__` on b) or give `TypeError`.