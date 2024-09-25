## Explanation of Concepts learnt in SoCo based on Software Design Book

We have the class `Shape` defined with its methods: `perimeter`and `area`:

```python3
class Shape:
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        raise NotImplementedError("perimeter")

    def area(self):
        raise NotImplementedError("area")
```
Where `__init__` is used to initialize objects of a class. It is also called a constructor.

This is considered a contact, because `Shape` has certain methods, and if we add new classes, e.g.: Circle and Square, then these must have the same methods as Shape.

-> Squares and Circles have the same methods, we can use them interchangeably. This is called **polymorphism**

-> The function call looks up the function stored in the dictionary, then calls that function with the dictionary as its first object

-> interpreter reads some source code and then transforms it into binary to execute-> as it goes, on the fly
-> compiler pre-compiles entire program, analyses and optimizes then translates to binary to execute