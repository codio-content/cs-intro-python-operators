---------

It is legal to add attributes to objects at any point in the execution of a program, but if you have objects with the same type that don’t have the same attributes, it is easy to make mistakes. It is considered a good idea to initialize all of an object’s attributes in the init method.

If you are not sure whether an object has a particular attribute, you can use the built-in function <span>hasattr</span> (see Section 15.7).

Another way to access attributes is the built-in function <span>vars</span>, which takes an object and returns a dictionary that maps from attribute names (as strings) to their values:

    >>> p = Point(3, 4)
    >>> vars(p)
    {'y': 4, 'x': 3}

For purposes of debugging, you might find it useful to keep this function handy:

    def print_attributes(obj):
        for attr in vars(obj):
            print(attr, getattr(obj, attr))

`print_attributes` traverses the dictionary and prints each attribute name and its corresponding value.

The built-in function <span>getattr</span> takes an object and an attribute name (as a string) and returns the attribute’s value.

