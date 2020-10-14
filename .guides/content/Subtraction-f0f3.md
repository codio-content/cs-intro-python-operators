----------

## Subtraction

```python
a = 10
b = 3
c = a - b
print(c)
```

{try it}(python3 code/operators/playground-subtract.py 1)

|||challenge
## What happens if you:
* Change `b` to `-3`?
* Change `c` to `c = a - -b`?
* Change `b` to `3.0`?
* Change `b` to `False`?

|||

{try it}(python3 code/operators/playground-subtract.py 2)

<details>
  <summary><b>Subtracting a Boolean?</b></summary>
  In Python, boolean value are more than just true and false. False has the numerical value of 0, while true has the numerical value of 1. This is why doing math with a boolean does not give you an error message.
</details>

## The `-=` Operator
Decrementing is the opposite of incrementing. Like `+=`, there is a shorthand for decrementing a variable - `-=`.

```python
a = 10
b = 3
a -= b
print(a)
```

{try it}(python3 code/operators/playground-subtract.py 3)

<details>
  <summary><strong>Subtraction and Strings</strong></summary>
  You might be able to concatenate strings with the <code>+</code> operator, but you cannot use the <code>-</code> operator with them.
</details>

{Check It!|assessment}(multiple-choice-3785924639)

