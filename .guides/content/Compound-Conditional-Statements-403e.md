----------

## Compound Conditional Statements

Conditional statements (if statements) are used to match an action with a condition being true. For example, print `Even` if a number is even. If you want to test for a number being even and greater than 10, you will need two conditionals.

```python
num = 16

if num % 2 == 0 and num > 10:
    print("Even and greater than 10")
```

{try it}(python3 code/selection/compound-conditionals.py 1)

|||challenge
## What happens if you:
* Change `num` to `8`?
* Change `and` to `or`?
* Change `==` to `!=`?

|||

{try it}(python3 code/selection/compound-conditionals.py 2)

## Why Use Compound Conditionals

Both code snippets below do the same thing: Ask if `my_var` is greater than 15 and if `my_var` is less than 20. If both of these are true, then Python will print the value of `my_var`.

![compound conditional](.guides/images/compound-conditional.png)

The code with the compound conditional (on the right) has fewer lines of code, and is easier for a human to read. In fact, it almost reads like a sentence.

{Check It!|assessment}(multiple-choice-3946834266)

