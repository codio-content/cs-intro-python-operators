----------

## Elif Syntax

The elif statement is written similarly to the if statement. There are few differences as well. Here are the rules for writing an elif statement:

* An if statement must come before the first elif statement
* `elif` is followed by a boolean expression and a `:`
* Indent four spaces and write the commands for when the elif statement is true
* You can write as many elif statements as you want
* An else statement must come after the last elif statement

<details><summary><b>What does `elif` mean?</b></summary>`elif` is an abbreviation of `else` and `if`. Since elif statements are common, the command was simplified so programmers would not have to write `else if`.</details>

![elif Statement](.guides/images/elif-statement.png)

```python
a = 20

if a < 10:
    print(str(a) + " is less than 10")
elif a < 20:
    print(str(a) + " is less than 20")
elif a < 30:
    print(str(a) + " less than 30")
else:
    print(str(a) + " is greater than 30")
```

[Code Visualizer](open_tutor code/selection/elif-syntax.py)
{try it}(python3 code/selection/elif-syntax.py 1)

|||challenge
## What happens if you:
* Change `a` to `0`?
* Change `a` to `100`?
* Change `a` to `30`? (How can you fix this?)

|||

[Code Visualizer](open_tutor code/selection/elif-syntax.py)
{try it}(python3 code/selection/elif-syntax.py 2)

{Check It!|assessment}(multiple-choice-1573332278)


