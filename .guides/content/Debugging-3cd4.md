---------

When you start working with objects, you are likely to encounter some new exceptions. If you try to access an attribute that doesn’t exist, you get an <span>AttributeError</span>:

    >>> p = Point()
    >>> p.x = 3
    >>> p.y = 4
    >>> p.z
    AttributeError: Point instance has no attribute 'z'

If you are not sure what type an object is, you can ask:

    >>> type(p)
    <class '__main__.Point'>

You can also use <span>isinstance</span> to check whether an object is an instance of a class:

    >>> isinstance(p, Point)
    True

If you are not sure whether an object has a particular attribute, you can use the built-in function <span>hasattr</span>:

    >>> hasattr(p, 'x')
    True
    >>> hasattr(p, 'z')
    False

The first argument can be any object; the second argument is a <span>*string*</span> that contains the name of the attribute.

You can also use a <span>try</span> statement to see if the object has the attributes you need:

    try:
        x = p.x
    except AttributeError:
        x = 0

This approach can make it easier to write functions that work with different types; more on that topic is coming up in Section [polymorphism].

