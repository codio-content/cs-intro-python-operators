----------------------------------

When you create a variable inside a function, it is <span>**local**</span>, which means that it only exists inside the function. For example:

    def cat_twice(part1, part2):
        cat = part1 + part2
        print_twice(cat)

This function takes two arguments, concatenates them, and prints the result twice. Here is an example that uses it:

    >>> line1 = 'Bing tiddle '
    >>> line2 = 'tiddle bang.'
    >>> cat_twice(line1, line2)
    Bing tiddle tiddle bang.
    Bing tiddle tiddle bang.

When `cat_twice` terminates, the variable <span>cat</span> is destroyed. If we try to print it, we get an exception:

    >>> print(cat)
    NameError: name 'cat' is not defined

Parameters are also local. For example, outside `print_twice`, there is no such thing as <span>bruce</span>.

