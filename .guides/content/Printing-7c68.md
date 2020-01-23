----------

## Newline Character
The `print` command automatically adds a newline character each time you use it. This is the default behavior. The code below will not print the two words on the same line.

```python
print("Hello")
print("world")
```

{Try it}(python3 code/fundamentals/playground-printing2.py 1)

![Newline Character](.guides/images/newline-character.png)

The text in red shows the newline character which is added even if you do not type it. (The newline character is what is inserted when you press "Enter" or "Return").

## Removing the Newline Character
Add `, end=''` (two quotes with nothing between them) to your `print` command. This overrides the default newline character.

```python
print("Hello ", end='')
print("world")
```

{Try it}(python3 code/fundamentals/playground-printing2.py 2)

|||challenge
## What happens if you:
* Use double quotes instead of single quotes with `end=''`
* Use `end='\t'` in the `print` command
* Use `end='!'` in the `print` command

|||

{Try it}(python3 code/fundamentals/playground-printing2.py 3)

{Check It!|assessment}(multiple-choice-3628483659)
