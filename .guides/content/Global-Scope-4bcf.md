## Global Scope - Referencing Variables

When a variable is declared inside a function, it has local scope. When a variable is declared in the main program, it has global scope. Global variables are declared outside of functions, but can be referenced inside a function.

![Global Scope 1](.guides/images/global-scope1.png)

```python
greeting = "Hello"

def say_hello():
    """Print a greeting"""
    print(greeting)

say_hello()
```

{try it}(python3 code/functions/global-scope.py 1)

There is a dotted line around the function because there are limitations on what can be done to global variables. 

|||challenge
## What happens if you:
* Modify `greeting` inside the function:
```python
greeting = "Hello"

def say_hello():
    """Print a greeting"""
    greeting = "Bonjour"
    print(greeting)

say_hello()
print(greeting)
```

|||

{try it}(python3 code/functions/global-scope.py 2)


## Global Scope - Modifying Variables

The suggestion above asked you to try and modify `greeting` inside the function. However, the output of the program did not change the value of the original `greeting`. Be default, you can reference a global variable in a function, but you cannot modify it. The `global` keyword allows you to modify global variables inside a function. In the image below, there is no more dotted line around the function. `global` removes the restriction for modifying `greeting`. That is why the output is `Bonjour` and `Bonjour`.

![Global Scope 2](.guides/images/global-scope2.png)

```python
greeting = "Hello"

def say_hello():
    """Demonstrate how to use the global keyword"""
    global greeting
    greeting = "Bonjour"
    print(greeting)

say_hello()
print(greeting)
```

{try it}(python3 code/functions/global-scope.py 3)

|||challenge
## What happens if you:
* Make the code look like this:
```python
def say_hello():
    """Demonstrate how to use the global keyword"""
    global greeting
    greeting = "Bonjour"
    print(greeting)

say_hello()
print(greeting)
```
* Flip the order of `say_hello()` and `print(greeting)`, and run the program again?

|||

{try it}(python3 code/functions/global-scope.py 4)

{Check It!|assessment}(multiple-choice-1787984748)
