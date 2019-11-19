----------

## If Statement

If statements test to see if a certain condition is true. If yes, then a specific commands are run. The simple if statement does not do anything if the boolean expression is false.

```python
if 7 != 10:
    print("The above statement is true")
print("This is not related to the if statement")
```

[Code Visualizer](open_tutor code/selection/if-statement.py)
{try it}(python3 code/selection/if-statement.py 1)

|||challenge
## What happens if you:
* Change `!=` to `==`?
* Change `7 == 10` to `True`?
* Change `True` to `False`?
* Remove the indentation on line 2?

|||

[Code Visualizer](open_tutor code/selection/if-statement.py)
{try it}(python3 code/selection/if-statement.py 2)

## Testing Multiple Cases

You will find yourself needing to test the same variable multiple times. Be sure that you set up your conditionals to test **all** possible values of the variable.

```python
grade = 90

if grade > 70:
    print("Congrats, you passed the class")
    
if grade < 70:
    print("Condolences, you did not pass the class")
```

[Code Visualizer](open_tutor code/selection/if-statement.py)
{try it}(python3 code/selection/if-statement.py 3)

|||challenge
## What happens if you:
* Change `grade` to `60`?
* Change `grade` to `70`?
* Change `grade > 70` to `grade >= 70`?

|||

[Code Visualizer](open_tutor code/selection/if-statement.py)
{try it}(python3 code/selection/if-statement.py 4)

{Check It!|assessment}(parsons-puzzle-1352008565)

