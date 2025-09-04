**What is Encapsulation?**

- Encapsulation means bundling data (attributes) and methods (functions) into a single unit (class) and controlling access to that data.

- `The goal`: restrict direct access to object data and prevent unintended modifications.

- It enforces data hiding and controlled access.

**How Encapsulation Works in Python**

- Unlike Java or C++, Python doesn’t have strict access modifiers (private, protected, public). Instead, it follows conventions:

- Public members: No underscore → accessible everywhere.

- Protected members: One underscore `_var` → internal use only (but still accessible).

- Private members: Double underscore `__var` → name-mangled (harder to access from outside).

**What is a Static Method?**

- A static method is a method that belongs to a class but does not depend on instance (self) or class (cls).

- Defined using the @staticmethod decorator.

- Used for utility/helper functions related to the class, but not tied to object or class state.