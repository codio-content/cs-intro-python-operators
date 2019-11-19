----------

## If Else Statement

The if else statement is used when you want something to specific to happen if the boolean expression is true and if you want something else to happen if it is false. 

```python
my_bool = True

if my_bool:
    print("The value of my_bool is true")
else:
    print("The value of my_bool is false")
```

[Code Visualizer]
{try it}(python3 code/selection/if-else-statement.py 1)

|||challenge
## What happens if you:
* Change the value of `my_bool` to `False`?
* Change the value of `my_bool` to `not True and not False`?

|||

{try it}(python3 code/selection/if-else-statement.py 2)

## Odd or Even

You can combine the if else statement with the modulo operator to determine if a number is odd or even:

* Modulo returns the remainder after division is performed
* Calculate the modulo (`%`) of any number and 2
* If the modulo is 0, then the number is even

```python
num = 4

if num % 2 == 0:
    print(str(num) + " is an even number")
else:
    print(str(num) + " is an odd number")
```

<details><summary>**Refresher:`str`**</summary>The `str` function is used to convert (also called type casting) the value of `num` into a string so that it can be joined (concatenated) with the other string.</details>

{try it}(python3 code/selection/if-else-statement.py 3)

|||challenge
## What happens if you:
* Change `num` to `3`?
* Change `num` to `0`?
* Change `num` to `-8`? 

|||

{try it}(python3 code/selection/if-else-statement.py 4)

{Check It!|assessment}(parsons-puzzle-2713895980)

