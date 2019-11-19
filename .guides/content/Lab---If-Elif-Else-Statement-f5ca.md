----------

## Tutorial Lab 4: If Elif Else Statements

If Elif Else statements allow you to write a series of questions about the value of a variable. This gives you more precision about the decisions you can make. Here are the rules for using if elif else statements:

* Start with the traditional if statement
* Use the `elif` keyword followed by a conditional and a `:`
* Use as many `elif` statements as necessary
* End with the `else` keyword

```python
michelin_stars = 3

if michelin_stars == 1:
    print("This is a very good restaurant")
elif michelin_stars == 2:
    print("This is an excellent restaurant")
else:
    print("This restaurant is among the best in the world")
```

[Code Visualizer](open_tutor code/selection/lab4.py)
{try it}(python3 code/selection/lab4.py 1)

The if elif else statements can also be faster than a series of if statements. As soon as a boolean expression is true, Python stops computing the remaining boolean expressions. Python will execute all of the if statements, even if one of them is true.

![Efficiency](.guides/images/efficiency-elif.png)

{Check It!|assessment}(parsons-puzzle-3355268222)