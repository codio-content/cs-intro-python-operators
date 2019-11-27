----------

## Whitespace

Whitespace refers to indentations and blank lines in your program. Indentations matter greatly for Python; your program can change greatly when indentation is not properly done. Notice that there is no function call in the code below. What do you think will happen when you run this program?

```python
def greet_twice():
    print("Hello")
print("Hello")
```

{try it}(python3 code/functions/whitespace.py 1)

So the first print statement does not run because there is no function call. However, the second print statement is not a part of the function definition because it is not indented. So it will run when the program is executed.

|||challenge
## What happens if you:
* Change the code to look like this:
```python
def greet_twice():
  print("Hello")
    print("Hello")
greet_twice()
```
* Change the code to look like this:
```python
def greet_twice():
  
  print("Hello")
  
  print("Hello")

greet_twice()
```
* Change the code to look like this:
```python
def greet_twice():
    print("Hello")
    print("Hello")
    greet_twice()
```

|||

{try it}(python3 code/functions/whitespace.py 2)

## Order Matters

The order of function definitions and function calls is important in Python. In the code below, the function call appears before the function definition. What do you think will happen when you run the code?

```python
greet_twice()

def greet_twice():
    print("Hello")
    print("Hello")
```

{try it}(python3 code/functions/whitespace.py 3)

Python says that `greet_twice` is not defined. But two lines later the function is clearly defined. Python requires that functions be defined before they are called. 

{Check It!|assessment}(multiple-choice-1748259403)
