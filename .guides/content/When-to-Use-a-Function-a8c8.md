----------

## Divide and Conquer

If you had to explain how to draw a house, you would make a list of shapes to draw. Draw a triangle for the roof, draw a square for the house, draw a rectangle for the door, etc. Combine all of these shapes, and you have a house. This approach to problem solving makes complex problems easier to understand, easier to solve, and easier to fix.

Functions allow for the same divide and conquer approach to problem solving but for programming. Each of the tasks above become a function. Combine all of the functions together, and you should have a house.

```python
import turtle

t = turtle.Turtle()

def roof():
    """Draw a triangle to represent a roof"""
    for i in range(3):
        t.lt(120)
        t.forward(100)

def house():
    """Draw a rectangle to represent a house"""
    for i in range(4):
        t.rt(90)
        t.forward(100)
        
roof()
house()

turtle.mainloop()
```

{Try it|terminal}(sh .guides/bg.sh python3 code/functions/when-functions.py)

|||challenge
## Add a Door
Write a new function that adds a door to the house. Hint, move the turtle to an appropriate starting position before drawing the door.
<details><summary>**One Possible Solution**</summary>Here is one possible solution. Remember to call the function in your program.<img src=".guides/images/turtle-door.png" /></details>

|||

{Try it|terminal}(sh .guides/bg.sh python3 code/functions/when-functions.py)

{Check It!|assessment}(multiple-choice-531814659)
