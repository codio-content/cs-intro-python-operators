
-----------------

To check whether you have the <span>turtle</span> module, use the Python interpreter in the terminal window and type

    >>> import turtle
    >>> bob = turtle.Turtle()
    

When you run this code, it should create a new window with small arrow that represents the turtle. Close the window.

Type this code into the <span>turtle_exercise_1.py</span>:

    import turtle
    bob = turtle.Turtle()
    print(bob)
    turtle.mainloop()

{Try It}(sh .guides/bg.sh python3 code/turtle_exercise_1.py)

The <span>turtle</span> module (with a lowercase ’t’) provides a function called <span>Turtle</span> (with an uppercase ’T’) that creates a Turtle object, which we assign to a variable named <span>bob</span>. Printing <span>bob</span> displays something like:

    <turtle.Turtle object at 0xb7bfbf4c>

This means that <span>bob</span> refers to an object with type <span>Turtle</span> as defined in module <span>turtle</span>.

`mainloop` tells the window to wait for the user to do something, although in this case there’s not much for the user to do except close the window.

Once you create a Turtle, you can call a <span>**method**</span> to move it around the window. A method is similar to a function, but it uses slightly different syntax. For example, to move the turtle forward:

    bob.fd(100)

The method, <span>fd</span>, is associated with the turtle object we’re calling <span>bob</span>. Calling a method is like making a request: you are asking <span>bob</span> to move forward.

The argument of <span>fd</span> is a distance in pixels, so the actual size depends on your display.

Other methods you can call on a Turtle are <span>bk</span> to move backward, <span>lt</span> for left turn, and <span>rt</span> right turn. The argument for <span>lt</span> and <span>rt</span> is an angle in degrees.

Also, each Turtle is holding a pen, which is either down or up; if the pen is down, the Turtle leaves a trail when it moves. The methods <span>pu</span> and <span>pd</span> stand for “pen up” and “pen down”.

To draw a right angle, add these lines to the program (after creating <span>bob</span> and before calling `mainloop`):

    bob.fd(100)
    bob.lt(90)
    bob.fd(100)

When you run this program, you should see <span>bob</span> move east and then north, leaving two line segments behind.

{Try It}(sh .guides/bg.sh python3 code/turtle_exercise_1.py)

Now modify the program to draw a square. Don’t go on until you’ve got it working!

