----------

## Tutorial Lab 2: If Else Statements

The if else statement gives your program the ability to ask a question, perform actions if the answer is true, and perform another set of actions if the answer is false.

```python
x = 10

if x > 50:
    print(str(x) + " is greater than 50")
else:
    print(str(x) + " is less than 50")
```

[Code Visualizer](open_tutor code/selection/lab2.py)
{try it}(python3 code/selection/lab2.py 1)

The if part of the if else statement is written as before. The `else` keyword is **not** indented; it should be aligned with the `if` keyword. `else` is followed by a `:`. You do not use a boolean expression with `else`. All code that should run when the boolean expression is false must be indented four spaces.

Be careful when expression your boolean expression in terms of "less than or greater than". This does not take into account when the values being compared are equal. Consider the code from above, but with `x` having the value of `50`.

```python
x = 50

if x > 50:
    print(str(x) + " is greater than 50")
else:
    print(str(x) + " is less than 50")
```

[Code Visualizer](open_tutor code/selection/lab2.py)
{try it}(python3 code/selection/lab2.py 2)

The output of the program does not make sense. 50 is not less than 50. Sometimes using `<=` and `>=` need to be used. Be sure to think through all of the possible outcomes, and make sure your code can function properly in all of those scenarios.

{Check It!|assessment}(parsons-puzzle-2074845473)