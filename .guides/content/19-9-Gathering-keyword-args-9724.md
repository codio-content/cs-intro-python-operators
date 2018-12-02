----------------------

In Section 12.4, we saw how to write a function that gathers its arguments into a tuple:

    def printall(*args):
        print(args)

You can call this function with any number of positional arguments (that is, arguments that don’t have keywords):

    >>> printall(1, 2.0, '3')
    (1, 2.0, '3')

But the operator doesn’t gather keyword arguments:

    >>> printall(1, 2.0, third='3')
    TypeError: printall() got an unexpected keyword argument 'third'

To gather keyword arguments, you can use the <span>\*</span> operator:

    def printall(*args, **kwargs):
        print(args, kwargs)

You can call the keyword gathering parameter anything you want, but <span>kwargs</span> is a common choice. The result is a dictionary that maps keywords to values:

    >>> printall(1, 2.0, third='3')
    (1, 2.0) {'third': '3'}

If you have a dictionary of keywords and values, you can use the scatter operator, <span>\*</span> to call a function:

    >>> d = dict(x=1, y=2)
    >>> Point(**d)
    Point(x=1, y=2)

Without the scatter operator, the function would treat <span>d</span> as a single positional argument, so it would assign <span>d</span> to <span>x</span> and complain because there’s nothing to assign to <span>y</span>:

    >>> d = dict(x=1, y=2)
    >>> Point(d)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: __new__() missing 1 required positional argument: 'y'

When you are working with functions that have a large number of parameters, it is often useful to create and pass around dictionaries that specify frequently used options.

