----------

## The `and` Operator

The `and` operator allows for compound (more than one) boolean expressions. All boolean expressions **must** be true in order for the whole thing to be true. If only one boolean expressions is false, then the whole thing is false.

```python
a = True
b = True
c = False
print(a and b)
```

{try it}(python3 code/operators/playground-and.py 1)

|||challenge
## What happens if you:
* Change `print` to `print(a and c)`?
* Change `print` to `print(c and b)`?

|||

{try it}(python3 code/operators/playground-and.py 2)

## Multiple `and` Statements

You can chain several `and` statements together. They are evaluated in a left-to-right manner.

```python
a = True
b = True
c = False
print(a and b and c)
```

{try it}(python3 code/operators/playground-and.py 3)

|||challenge
## What happens if you:
* Change `print` to `print(a and b and a and b and a)`?
* Change `print` to `print(a and b and a and b and c)`?

|||

{try it}(python3 code/operators/playground-and.py 4)


{Check It!|assessment}(fill-in-the-blanks-583769072)

