**What is an Abstract Class?**

- An abstract class is a class that cannot be instantiated directly. - It serves as a blueprint for other classes.

- Abstract classes can contain abstract methods (methods without implementation) and concrete methods (regular methods with implementation).

- They are useful when you want derived classes to implement specific methods while sharing some common functionality.

**Why Use Abstract Classes?**

- To enforce a common interface across multiple subclasses.
- To ensure that certain methods must be implemented by all subclasses.
- To provide common behavior in one place, reducing code duplication.

**`abc` Module in Python**

- Python provides the `abc` module to define abstract classes and methods:
- `ABC`: Base class to define an abstract class.
- `@abstractmethod`: Decorator to declare a method as abstract.

```python
from abc import ABC, abstractmethod
```
**Basic Example**
```python
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass  # No implementation
    
    @abstractmethod
    def perimeter(self):
        pass

# Cannot create object of abstract class
# s = Shape()  # ❌ This will raise TypeError

# Subclass implementing abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Using the subclass
r = Rectangle(5, 10)
print("Area:", r.area())          # Area: 50
print("Perimeter:", r.perimeter())  # Perimeter: 30

```
✅ Key Points:

- Shape is abstract → cannot instantiate.

- Rectangle implements all abstract methods → can instantiate.

- If a subclass does not implement all abstract methods, it also becomes abstract.**

**Concrete + Abstract Methods Together**
`Abstract classes can have normal methods too.`
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def fuel_type(self):
        pass
    
    def start_engine(self):
        print("Engine started...")

class Car(Vehicle):
    def fuel_type(self):
        return "Petrol"

c = Car()
c.start_engine()          # Engine started...
print(c.fuel_type())       # Petrol
```
`✅ Notice`: start_engine is already implemented, so subclasses inherit it.