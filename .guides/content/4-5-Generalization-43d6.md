--------------

The next step is to add a <span>length</span> parameter to <span>square</span>. Here is a solution:

    def square(t, length):
        for i in range(4):
            t.fd(length)
            t.lt(90)

    square(bob, 100)

Adding a parameter to a function is called <span>**generalization**</span> because it makes the function more general: in the previous version, the square is always the same size; in this version it can be any size.

{Try It}(sh .guides/bg.sh python3 code/turtle_world.py)

The next step is also a generalization. Instead of drawing squares, <span>polygon</span> draws regular polygons with any number of sides. Here is a solution:

    def polygon(t, n, length):
        angle = 360 / n
        for i in range(n):
            t.fd(length)
            t.lt(angle)

    polygon(bob, 7, 70)

This example draws a 7-sided polygon with side length 70.

If you are using Python 2, the value of <span>angle</span> might be off because of integer division. A simple solution is to compute <span>angle = 360.0 / n</span>. Because the numerator is a floating-point number, the result is floating point.

When a function has more than a few numeric arguments, it is easy to forget what they are, or what order they should be in. In that case it is often a good idea to include the names of the parameters in the argument list:

    polygon(bob, n=7, length=70)

These are called <span>**keyword arguments**</span> because they include the parameter names as “keywords” (not to be confused with Python keywords like <span>while</span> and <span>def</span>).

This syntax makes the program more readable. It is also a reminder about how arguments and parameters work: when you call a function, the arguments are assigned to the parameters.

