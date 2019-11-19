## Tutorial Lab 1: Arithmetic Operators

Arithmetic operations in Python are mostly the same as what you learned in math class. However, the symbols used in Python can be different.

|Operation|Symbol|Notes|
|---------|------|-----|
|Addition | + | |
|Subtraction | - | |
|Multiplication | * | |
|Division | / |Always returns a float|
|Floor Division | // |Truncates the answer to be an integer|
|Power (exponent) | ** |The inverse of the exponent will return a root|
|Modulo | % | Returns the remainder after division is performed|

Use the text editor open in the left pane, and enter the following code:

```python
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3)
```

{Try it}(python3 code/operators/lab-arithmetic-operators.py)

To see what is happening in these calculations, click [here](open_tutor code/operators/lab-arithmetic-operators.py). Click on the `Forward >` button to see how the calculations progress step by step.
1) Addition works as expected.
2) Subtraction works as expected.
3) Multiplication works as expected.
4) Division will always return a float, even if you are dividing two integers.
5) Floor division returns `3` because everything after the decimal point is ignored. The result is not rounded up or down.
6) Modulo returns `1` because that is the remainder (not the decimal) after division is performed.

{Check It!|assessment}(fill-in-the-blanks-977027531)