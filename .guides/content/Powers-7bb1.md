----------

## Powers

Python uses the `**` operator for powers (or exponents). So `2 ** 2` would be two to the second power.

```python
a = 2 ** 2
print(a)
```

{try it}(python3 code/operators/playground-powers.py 1)

|||challenge
## What happens if you:
* Change `a` to `2 ** 0`?
* Change `a` to `2 ** -2`?
* Change `a` to `2 ** False`?

|||

{try it}(python3 code/operators/playground-powers.py 2)

## Square Root

The square root of 4 can be calculated as 4 raised to the power of $\frac{1}{2}$. In Python, this is written as `4 ** 0.5`.

<details>
  <summary><b>The </b><code>sqrt</code><b> function</b></summary>
  Python does have a <code>sqrt</code> function, but it requires you to import the <code>math</code> library. Libraries will be covered in a later lesson.
  
  ```python
  import math
  
  square_root = math.sqrt(4)
  print(square_root)
  ```
  
</details>

```python
square_root = 4 ** 0.5
print(square_root)
```

{try it}(python3 code/operators/playground-powers.py 3)

{Check It!|assessment}(multiple-choice-2214264847)
