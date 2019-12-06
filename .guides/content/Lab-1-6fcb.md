## Lab 1

If you start to zoom in on fractals, you will see the same shapes repeat themselves. Fractals are said to be self-similar, which means they can be drawn with recursion. This lab will walk you though drawing a [Sierpinski triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle). Start by preparing the program to use Python's turtle graphics. Sierpinski triangles can become quite complex, so increase the turtle's speed to 10 (the maximum).

```python
import turtle

t = turtle.Turtle()
t.speed(10)

turtle.mainloop()
```

The building block of this fractal is the triangle. Create a function (with a parameter for length) to draw a triangle. The turtle will be walking all over the screen, so it is important to make sure that the turtle is facing a consistent position before drawing the triangle. `t.setheading(180)` ensures the turtle is facing to the left.

```python
import turtle

t = turtle.Turtle()
t.speed(10)
         
def draw_triangle(length):
    t.setheading(180)      
    for i in range(3):     
        t.rt(120)          
        t.fd(length)

draw_triangle(50)

turtle.mainloop()
```

{Try it|terminal}(sh .guides/bg.sh python3 code/functions/lab1.py)

Look closely at a Sierpinski triangle, and you will see clusters of three triangles that make up clusters of triangles and so forth.

![Sierpinski Triangle Evolution](.guides/images/Sierpinski_triangle_evolution.svg)

You are now going to create a recursive function that draws this cluster of three triangles. Define the function `sierpinski` that takes `length` and `n` as parameters. The base case is if `n` is equal to 1. If so, draw a triangle of size `length`. If `n` is not equal to 1, then you are going to call `sierpinski` again, but with `n-1`. These new triangles need to be in a different position, so move the turtle after drawing each turtle. Finally, replace the `draw_triangle` function call with `sierpinski(50, 1)`.

```python
import turtle

t = turtle.Turtle()
t.speed(10)

def sierpinski(length, n):
    if n == 1:
        draw_triangle(length)
    else:
      sierpinski(length, n-1)
      t.rt(120)
      t.fd(length)
      sierpinski(length, n-1)
      t.lt(120)               
      t.fd(length) 
      sierpinski(length, n-1)
      t.fd(length)  
         
def draw_triangle(length):
    t.setheading(180)      
    for i in range(3):     
        t.rt(120)          
        t.fd(length)

sierpinski(50, 1)

turtle.mainloop()
```

{Try it|terminal}(sh .guides/bg.sh python3 code/functions/lab1.py)

|||challenge
## What happens if you:
* Change the function call to `sierpinski(50, 2)`?
* Change the function call to `sierpinski(50, 3)`?
* Change the function call to `sierpinski(50, 4)`?

|||

{Try it|terminal}(sh .guides/bg.sh python3 code/functions/lab1.py)

The triangles are clustered together, but the Sierpinski triangle has larger triangle-shaped voids. An adjustment needs to be made to the distance the turtle moves between calls to the `sierpinski` function. Instead of moving forward the distance of `length`, the turtle will move forward `length * (n-1)`. Change the `sierpinski` function call to `sierpinski(20, 4)`.

```python
import turtle

t = turtle.Turtle()
t.speed(10)

def sierpinski(length, n):
    if n == 1:
        draw_triangle(length)
    else:
      sierpinski(length, n-1)
      t.rt(120)
      t.fd(length * (n-1))
      sierpinski(length, n-1)
      t.lt(120)               
      t.fd(length * (n-1)) 
      sierpinski(length, n-1)
      t.fd(length * (n-1))  
         
def draw_triangle(length):
    t.setheading(180)      
    for i in range(3):     
        t.rt(120)          
        t.fd(length)

sierpinski(20, 4)

turtle.mainloop()
```

{Try it|terminal}(sh .guides/bg.sh python3 code/functions/lab1.py)

The fractal is getting better, but there are a few areas where the program can be improved. Change the distance the turtle goes forward from `t.fd(length * (n-1))` to `t.fd(length * 2 ** (n-2))`.

```python
import turtle

t = turtle.Turtle()
t.speed(10)

def sierpinski(length, n):
    if n == 1:
        draw_triangle(length)
    else:
      sierpinski(length, n-1)
      t.rt(120)
      t.fd(length * 2**(n-2))
      sierpinski(length, n-1)
      t.lt(120)               
      t.fd(length * 2**(n-2)) 
      sierpinski(length, n-1)
      t.fd(length * 2**(n-2))  
         
def draw_triangle(length):
    t.setheading(180)      
    for i in range(3):     
        t.rt(120)          
        t.fd(length)

sierpinski(20, 4)

turtle.mainloop()
```

{Try it|terminal}(sh .guides/bg.sh python3 code/functions/lab1.py)

|||challenge
## What happens if you:
* Change the `sierpinski` function call to `sierpinski(5, 6)`?
* Change the `sierpinski` function call to `sierpinski(5, 8)`?

|||

{Try it|terminal}(sh .guides/bg.sh python3 code/functions/lab1.py)