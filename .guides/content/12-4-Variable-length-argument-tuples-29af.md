-------------------------------

Functions can take a variable number of arguments. A parameter name that begins with <span>**gathers**</span> arguments into a tuple. For example, <span>printall</span> takes any number of arguments and prints them:

    def printall(*args):
        print(args)

The gather parameter can have any name you like, but <span>args</span> is conventional. Here’s how the function works:

    >>> printall(1, 2.0, '3')
    (1, 2.0, '3')

The complement of gather is <span>**scatter**</span>. If you have a sequence of values and you want to pass it to a function as multiple arguments, you can use the operator. For example, <span>divmod</span> takes exactly two arguments; it doesn’t work with a tuple:

    >>> t = (7, 3)
    >>> divmod(t)
    TypeError: divmod expected 2 arguments, got 1

But if you scatter the tuple, it works:

    >>> divmod(*t)
    (2, 1)

Many of the built-in functions use variable-length argument tuples. For example, <span>max</span> and <span>min</span> can take any number of arguments:

    >>> max(1, 2, 3)
    3

But <span>sum</span> does not.

    >>> sum(1, 2, 3)
    TypeError: sum expected at most 2 arguments, got 3

As an exercise, write a function called <span>sumall</span> that takes any number of arguments and returns their sum.

