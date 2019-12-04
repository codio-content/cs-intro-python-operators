## Modularity

Another benefit to using functions in your programs is modularity. Modularity means dividing a program into separate and independent units. In a previous lesson, you used Python's turtle graphics to draw a house. Think about how you would write functions to draw the following image. The red dots represents the starting points for each of the shapes. Look for repeating patterns and think about how these patterns could be represented in a modular way.

![House](.guides/images/house.png)

The image is composed of two shapes: a rectangle (a square is a rectangle with four sides of equal length) and a triangle. You also need the ability to reposition the turtle without drawing any lines on the screen. These are the three functions that will make up the drawing.

```python
import turtle

t = turtle.Turtle()

def triangle(size):
    """Draw a triangle with a given size"""
    for i in range(3):
        t.lt(120)
        t.forward(size)

def rectangle(width, height):
    """Draw a rectangle with a given width and height"""
    for i in range(2):
        t.forward(width)
        t.lt(90)
        t.forward(height)
        t.lt(90)
        
def reposition(x, y):
    """Pick up the pen, move the turtle, set the
    direction of the turtle, and put the pen down"""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
        
rectangle(100, 100) #draw the house
reposition(100, 100) #move to starting point for the roof
triangle(100) #draw the roof
reposition(40, 0) #move to starting point for the door
rectangle(20, 40) #draw the door
reposition(10, 50) #move to starting point for the left window
rectangle(20, 20) #draw the left window
reposition(70, 50) #move to starting point for the right window
rectangle(20, 20) #draw the right window

turtle.mainloop()
```

{Try it|terminal}(sh .guides/bg.sh python3 code/functions/modularity.py)

These functions are modular in that each one draws a shape. More importantly, the functions were written with parameters to specify the size of each shape. Modularity makes functions reusable. This way you do not have write a function for the house, another for the door, and a third for the windows.

|||challenge
## Tiny House
Change the code to draw a house that is half of the size of the original.
<details><summary>**Solution**</summary><img src=".guides/images/small-house.png" /></details>

|||

{Try it|terminal}(sh .guides/bg.sh python3 code/functions/modularity.py)

{Check It!|assessment}(multiple-choice-2677448801)
