----------

## Incrementing Variables
Incrementing a variable means to change the value of a variable by a set amount. You will most often have a counting variable, which means you will increment by 1.

```python
a = 0
a = a + 1
print(a)
```

{try it}(python3 code/operators/playground-increment.py 1)

## How to Read `a = a + 1`
The variable `a` appears twice on the same line of code. But each instance of `a` refers to something different.

![How to Read a = a + 1](.guides/images/increment.png)

## The `+=` Operator
Incrementing is a common task for programmers. Many programming languages have developed a shorthand for `a = a + 1` because of this. `a += 1` does the same thing as `a = a + 1`.

```python
a = 0
b = 0
a = a + 1
b += 1
print(a)
print(b)
```

{try it}(python3 code/operators/playground-increment.py 2)

|||challenge
## What happens if you:
* Change `b` such that `b += 2`?
* Change `b` such that `b += -1`?
* Change `b` such that `b -= 1`?

|||

{try it}(python3 code/operators/playground-increment.py 3)

{Check It!|assessment}(multiple-choice-905140979)
