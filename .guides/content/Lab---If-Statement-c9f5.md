----------

## Tutorial Lab 1: If Statements

The if statement allows for your program to make a decision about what it should do. It asks a simple question, is this condition true? If yes, then the computer will execute certain commands.

```python
x = 5

if x < 10:
    print("Less than 10")
```

[Code Visualizer](open_tutor code/selection/lab1.py)
{try it}(python3 code/selection/lab1.py 1)

An if statement is comprised of the keyword `if`, followed by a boolean expression, and a `:`. Any code that should run if the boolean expression is true must be indented. In Python, programmers indent four spaces.

If the boolean expression is false, the indented code is skipped, and the program continues as normal.

```python
x = 20

if x < 10:
    print("Less than 10")
    
print("And the program continues...")
```

[Code Visualizer](open_tutor code/selection/lab1.py)
{try it}(python3 code/selection/lab1.py 2)

{Check It!|assessment}(multiple-choice-3649559415)