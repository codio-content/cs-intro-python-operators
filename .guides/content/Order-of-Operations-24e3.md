----------

## Order of Operations

Python uses the PEMDAS method for determining order of operations.

![PEMDAS](.guides/images/pemdas.png)

The code below should output `7.0`.

```python
a = 2
b = 3
c = 4
result = 3 * a ** 3 / (b + 5) + c
print(result)
```

{try it}(python3 code/operators/playground-pemdas.py 1)

<details><summary><b>Explanation</b></summary><ul><li>The first step is to compute `b + 5` (which is `8`) because it is surrounded by parentheses.</li><li>Next, calculate `a ** 3` (which is `8`) because it is an exponent.</li><li>Next, do the multiplication and division going from left to right. `3 * 8` is `24`.</li><li>`24` divided by `8` is `3.0` (remember, the `/` operator returns a float).</li><li>Finally, add `3.0` and `4` together to get `7.0`.</li></ul></details>

|||challenge
## Mental Math
* `5 + 7 - 10 * 3 /0.5`
<details><summary>Solution</summary>-48.0</details>
* `(5 * 8) - 7 ** 2 - (-1 * 18)`
<details><summary>Solution</summary>9</details>
* `9 / 3 + (100 ** 0.5) - 3`
<details><summary>Solution</summary>10.0</details>

|||

{try it}(python3 code/operators/playground-pemdas.py 1)

{Check It!|assessment}(parsons-puzzle-3925273068)

