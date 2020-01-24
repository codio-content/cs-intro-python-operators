----------

## Infinite Loops Are Bad, Right?
Well, that depends. If an infinite loop caused because the counting variable isn't incremented, then yes that is a bad thing. But some programmers purposely create a condition that will always evaluate to true. Therefore, the loop will always run. However, a `break` statement is used to stop the loop when a certain condition is true. Copy/paste the code below, and run it several times.

```python
import random
 
while True:
    print("This is an infinite loop")
    rand_num = random.randint(1, 101) # random integer between 1 and 100
    if rand_num > 75:
        print("The loop has ended")
        break # stop the loop
```

[Code Visualizer](open_tutor code/loops/playground-break-statement.py)
{Try it}(python3 code/loops/playground-break-statement.py 1)

Even though `while True` will always evaluate as a true statement, the loop never becomes infinite because of the `break` statement.

|||challenge
## What happens if you:
* Remove the `break` statement?
* Move the `break` statement to before the `print` statement?

|||

[Code Visualizer](open_tutor code/loops/playground-break-statement.py)
{Try it}(python3 code/loops/playground-break-statement.py 1)

### Comparing While Loops
Even though the while loops introduced on the previous page look different than the while loops covered on this page, they both have the same components and do the same thing.

![Comparing While Loops](.guides/images/comparing-while-loops.png)

{Check It!|assessment}(multiple-choice-3591284404)
