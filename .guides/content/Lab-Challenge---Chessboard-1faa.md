## Loops Challenge
For this challenge, you will output a pattern that resembles a chessboard by using the letter `X` and `O`. The pattern needs to be an 8 x 8 matrix with alternating `X` and `O` in each row. Here is the catch, you must also ensure that alternate rows start with a different letter than the previous row.

Here is an example of the output required.

```python
XOXOXOXO
OXOXOXOX
XOXOXOXO
OXOXOXOX
XOXOXOXO
OXOXOXOX
XOXOXOXO
OXOXOXOX
```

You should make use of a looping structure in combination with a decision structure to achieve this result. Also, by default, Python’s `print()` function will add the newline character at the end of each `print()` function so to ensure that this newline does not create a long, single column output of the letters, use this syntax for your `print()` functions, `print(‘X’, end=’’)`. Note the use of , `end=’’` after the letter to output.

{Try it}(python3 code/loops/lab-challenge.py)
{Check It!|assessment}(code-output-compare-1829566628)
