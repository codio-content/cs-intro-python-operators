## Tutorial Lab 4: Boolean Operators

Boolean operators are those operators which will return either true or false.

|Operation|Symbol|Notes|
|---------|------|-----|
|Equal to| ==| The `=` operator is assignment operator, not the equality operator|
|Not equal to| !=| |
|Less than| <| |
|Less than or equal to| <=| |
|Greater than| >| |
|Greater than or equal to| >=| |
|And | `and` | Compares two boolean expressions. Both must be true for the whole to be true. Everything else is false.|
|Or | `or` | Compares two boolean expressions. Both must be false for the whole to be false. Everything else is true.|
|Not | `not` | Returns the opposite of a boolean expression.|

Use the text editor open in the left pane, and enter the following code:

```python
print((5 > 7) and (False or 1 < 9) or 4 != 5 and not 2 >= 3)
```

{Try it}(python3 code/operators/lab-boolean-operators.py)

Unfortunately, the [code visualizer](open_tutor code/operators/lab-order-of-operations.py) is not very helpful. It executes an entire line of code, so you will not see each of the boolean expressions being evaluated. Below are the steps that Python talks when evaluating the code above.
1) `(5 > 7) and (False or 1 < 9) or 4 != 5 and not 2 >= 3`
2) `False and (False or 1 < 9) or 4 != 5 and not 2 >= 3`
3) `False and (False or True) or 4 != 5 and not 2 >= 3`
4) `False and True or 4 != 5 and not 2 >= 3`
5) `False and True or True and not 2 >= 3`
6) `False and True or True and not False`
7) `False and True or True and True`
8) `False or True and True`
9) `True and True`
10) `True`

{Check It!|assessment}(multiple-choice-1194669827)