----------

## Iteration with While Loops

For loops are almost exclusively used to iterate over lists. It is possible to use a while loop. Be aware of all of things you manually do when using a while loop over a for loop.

```python
numbers = [1, 2, 3, 4]
length = len(numbers)
i = 0

while i < length:
    print(numbers[i])
    i += 1
```

[Code Visualizer](open_tutor code/lists/list-while-loop.py)
{try it}(python3 code/lists/list-while-loop.py 1)

|||challenge
## What happens if you:
* Change the loop to `while i <= length:`?
* Change the `print` statement to `print(i)`?
* Remove `i += 1`?

|||

{try it}(python3 code/lists/list-while-loop.py 2)

## Comparing While & For Loops

![While and For Loops](.guides/images/compare-for-while-loops-iteration.png)

The for loop is more efficient than a while loop when iterating over a list. You do not need to declare variables for the length of the list (red text), declare a variable for the index of the list (blue text), or increment the index variable (orange text). All of this is handled by the `in` statement. In for loops, you can use the iteration variable to reference the list element. With a while loop, however, you need to use the list and index to reference the element (purple text).

{Check It!|assessment}(multiple-choice-4064533170)

