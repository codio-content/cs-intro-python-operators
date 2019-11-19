----------

## Tutorial Lab 3: Compound Conditionals

Sometimes you need to have two more things to be true before specific code can run. These are called compound conditionals because there are multiple boolean expressions in the conditional statement. The boolean expressions need to be linked together with either the `and` or `or` statements.

```python
x = 10

if x > 5 and x < 15:
    print(str(x) + " is between 5 and 15")
else:
    print(str(x) + " is not between 5 and 15")
```

[Code Visualizer](open_tutor code/selection/lab3.py)
{try it}(python3 code/selection/lab3.py 1)

The code above will be true for any number that is greater than 5 and less than 15. If `x` has the value of `5` or `15`, then the boolean expression will be false.

![Compound Conditional And](.guides/images/compound-conditional-and.png)

If you take the same code and change `and` to `or`, you get a very different program.

```python
x = 10

if x > 5 or x < 15:
    print(str(x) + " is between 5 and 15")
else:
    print(str(x) + " is not between 5 and 15")
```

[Code Visualizer](open_tutor code/selection/lab3.py)
{try it}(python3 code/selection/lab3.py 2)

It does not matter what value you give to `x`, the boolean expression will always be true. The boolean expression is true even if `x` is `5` or `15`.

![Compound Conditional Or](.guides/images/compound-conditional-or.png)

{Check It!|assessment}(multiple-choice-946441677)