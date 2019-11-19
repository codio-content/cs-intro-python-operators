## Tutorial Lab 2: for loop for calculating powers (exponents)
Use the text editor open in the left pane, and enter the following code:

```python
exp = 4
base = 2
result = 1
for x in range(exp):
    result = base * result
    
print(result)
```

{Try it}(python3 code/loops/lab-range.py)

Click [here](open_tutor code/loops/lab-range.py) to see the loop run in the code visualizer.

This is a crude way of calculating powers (in the example above it would be 2 to the power of 4), but it demonstrates the use of a for loop in an interesting way.
1) First off, we create `exp` (represents the exponent) and assign it the value of `4`.
2) Then we create `base` and assign it the value of `2`.
3) `result` (the final value of our program) is assigned the value of `1`.
4) The for loop will run `exp` number of times. In this case, it will run 4 times
5) The calculation takes `result` and multiplies it by `base` and assigns it back to itself. This is essentially how the power function works, you are multiplying a value by itself a specified number of times.
    * When `x` is `0`, `result` is assigned `2 * 1`, which is `2`.
    * When `x` is `1`, `result` is assigned `2 * 2`, which is `4`.
    * When `x` is `2`, `result` is assigned `2 * 4`, which is `8`.
    * When `x` is `3`, `result` is assigned `2 * 8`, which is `16`.
    * Finally, `result` is printed to the screen.
    
{Check It!|assessment}(multiple-choice-3013013327)