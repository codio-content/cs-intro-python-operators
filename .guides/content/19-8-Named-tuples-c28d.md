------------

Many simple objects are basically collections of related values. For example, the Point object defined in Chapter 15 contains two numbers, <span>x</span> and <span>y</span>. When you define a class like this, you usually start with an init method and a str method:

    class Point:

        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def __str__(self):
            return '(%g, %g)' % (self.x, self.y)

This is a lot of code to convey a small amount of information. Python provides a more concise way to say the same thing:

    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])

The first argument is the name of the class you want to create. The second is a list of the attributes Point objects should have, as strings. The return value from <span>namedtuple</span> is a class object:

    >>> Point
    <class '__main__.Point'>

<span>Point</span> automatically provides methods like `__init__` and `__str__` so you don’t have to write them.

To create a Point object, you use the Point class as a function:

    >>> p = Point(1, 2)
    >>> p
    Point(x=1, y=2)

The init method assigns the arguments to attributes using the names you provided. The str method prints a representation of the Point object and its attributes.

You can access the elements of the named tuple by name:

    >>> p.x, p.y
    (1, 2)

But you can also treat a named tuple as a tuple:

    >>> p[0], p[1]
    (1, 2)

    >>> x, y = p
    >>> x, y
    (1, 2)

Named tuples provide a quick way to define simple classes. The drawback is that simple classes don’t always stay simple. You might decide later that you want to add methods to a named tuple. In that case, you could define a new class that inherits from the named tuple:

    class Pointier(Point):
        # add more methods here

Or you could switch to a conventional class definition.

