**What is Inheritance (and why use it)?**

- Inheritance lets a class (the child/subclass) reuse and extend behavior/data from another class (the parent/base/superclass).

- Reuse: avoid rewriting shared code.

- Specialize: override or add new behavior in children.

- Polymorphism: different subclasses can be used through a common interface.

**Types of Inheritance with Code**

`1. Single Inheritance`

One parent → one child.
```python
class Vehicle: ...
class Car(Vehicle): ...
```

`2. Multilevel Inheritance`

Grandparent → Parent → Child.
```python
class LivingThing:
    pass

class Animal(LivingThing):
    pass

class Mammal(Animal):
    pass
```
`3. Multiple Inheritance`

Child inherits from multiple parents.
```python
class JSONSerializable:
    def to_json(self): ...

class Validatable:
    def validate(self): ...

class User(JSONSerializable, Validatable):
    pass
```

`4. Hierarchical Inheritance`

One parent → many children.
```python
class Shape: ...
class Circle(Shape): ...
class Rectangle(Shape): ...
```
`5.Hybrid Inheritance`

Combo of the above (often with a diamond).
```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass   # diamond (A at the top)
```