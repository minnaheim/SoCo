## Explanation of Concepts learnt in SoCo based on Software Design Book

# Week 1:

## Methods and Classes
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

## Arguments vs. Parameters:
we call the values passed into a function its arguments and the names the function uses to refer to them as its parameters. Put another way, parameters are part of the definition, and arguments are given when the function is called.

```python3
def sums(num1, num2)
    return num1 + num2

sums(1,3)
```
Where the parameters are num1 and num2 and the arguments here are 1,3.

## Inheritance

We add another specially-named field to the dictionaries for “classes” like Square to keep track of their parents:

we need to implement constructors. We do this by giving the dictionaries that implement classes a special key _new whose value is the function that builds something of that type:

-> The function call looks up the function stored in the dictionary, then calls that function with the dictionary as its first object

-> interpreter reads some source code and then transforms it into binary to execute-> as it goes, on the fly
-> compiler pre-compiles entire program, analyses and optimizes then translates to binary to execute

# Week 3
## Variable Scope
determines where the variable is accessible (i.e. which lines of code?)

- local scope: variables defined in a function
- enclosing scope: in the outer function of a nested function 
- global scope: defined outside of functions
- built-in scope: reserved in python3 defined globally.  -> like: print(), len()

How does Py check where it is defined?
Rule: LEGB -> local, enclosed, global, built in


## Stack 
Stack is a data structure that operates on a LIFO: Last In First Out 

Key Operations:
- push: add an element to the top (in list, last element)
- pop: remove top element
- peek: look at top element without removing it 

## Call Stack
Special type of stack used to manage function calls in python
when a function is called, its execution context (local variables, state) is pushed onto the stack

here, if we define x = 10 in the global (frame) stack f1 with x = 12, and f2,, and we have f2 nested in f1, then once we execute f2, we remove that stack, and then once we executre f1, we remove that stack and only keep the global stack
-> if we call x in the f2 stack, then which value of x do we get? f1's or global value?

Depends on whether interpreter uses lexical or dynamic scope:
- lexical: depends on where funciton is written. -> meaning x = 10, if f2 isn't def in f1, then x = 10
- dynamic: depends on which function is called where -> here x = 12 -> bec. defined in previous env?