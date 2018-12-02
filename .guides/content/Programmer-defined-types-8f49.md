------------------------

We have used many of Python’s built-in types; now we are going to define a new type. As an example, we will create a type called <span>Point</span> that represents a point in two-dimensional space.

In mathematical notation, points are often written in parentheses with a comma separating the coordinates. For example, $(0,0)$ represents the origin, and $(x,y)$ represents the point $x$ units to the right and $y$ units up from the origin.

There are several ways we might represent points in Python:

-   We could store the coordinates separately in two variables, <span>x</span> and <span>y</span>.

-   We could store the coordinates as elements in a list or tuple.

-   We could create a new type to represent points as objects.

Creating a new type is more complicated than the other options, but it has advantages that will be apparent soon.

A programmer-defined type is also called a <span>**class**</span>. A class definition looks like this:

    class Point:
        """Represents a point in 2-D space."""

The header indicates that the new class is called <span>Point</span>. The body is a docstring that explains what the class is for. You can define variables and methods inside a class definition, but we will get back to that later.

Defining a class named <span>Point</span> creates a <span>**class object**</span>.

    >>> Point
    <class '__main__.Point'>

Because <span>Point</span> is defined at the top level, its “full name” is `__main__.Point`.

The class object is like a factory for creating objects. To create a Point, you call <span>Point</span> as if it were a function.

    >>> blank = Point()
    >>> blank
    <__main__.Point object at 0xb7e9d3ac>

The return value is a reference to a Point object, which we assign to <span>blank</span>.

Creating a new object is called <span>**instantiation**</span>, and the object is an <span>**instance**</span> of the class.

When you print an instance, Python tells you what class it belongs to and where it is stored in memory (the prefix <span>0x</span> means that the following number is in hexadecimal).

Every object is an instance of some class, so “object” and “instance” are interchangeable. But in this chapter I use “instance” to indicate that I am talking about a programmer-defined type.

