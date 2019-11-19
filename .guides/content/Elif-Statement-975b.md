----------

## Elif Statement

The if statement asks a single question, "Is this true?". The if else statement asks two questions, "Is this true, or is this false?". The elif statement is used after an if statement and before an else statement. Elif statements give you more precision when making decisions.

![elif Statement](.guides/images/if-vs-else-vs-elif.png)

```python
grade = 82

if grade < 70:
    print("You got an F.")
elif grade < 80:
    print("You got a C.")
elif grade < 90:
    print("You got a B.")
else:
    print("You got an A.")
```

[Code Visualizer](open_tutor code/selection/elif-statement.py)
{try it}(python3 code/selection/elif-statement.py 1)

|||challenge
## Can you...
Add the letter grade D which is any grade from 60 to 69?

**Testing Your Code**
Change `grade` to `65`. You should see `You got a D.` as the output of your program.
<details><summary>**Hint**</summary>You need to change the if statement and add another elif statement.</details>

|||

[Code Visualizer](open_tutor code/selection/elif-statement.py)
{try it}(python3 code/selection/elif-statement.py 2)

