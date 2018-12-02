--------------

We have already seen one example of a <span>**function call**</span>:

    >>> type(42)
    <class 'int'>

The name of the function is <span>type</span>. The expression in parentheses is called the <span>**argument**</span> of the function. The result, for this function, is the type of the argument.

It is common to say that a function “takes” an argument and “returns” a result. The result is also called the <span>**return value**</span>.

Python provides functions that convert values from one type to another. The <span>`int`</span> function takes any value and converts it to an integer, if it can, or complains otherwise:

    >>> int('32')
    32
    >>> int('Hello')
    ValueError: invalid literal for int(): Hello

<span>`int`</span> can convert floating-point values to integers, but it doesn’t round off; it chops off the fraction part:

    >>> int(3.99999)
    3
    >>> int(-2.3)
    -2

<span>`float`</span> converts integers and strings to floating-point numbers:

    >>> float(32)
    32.0
    >>> float('3.14159')
    3.14159

Finally, <span>`str`</span> converts its argument to a string:

    >>> str(32)
    '32'
    >>> str(3.14159)
    '3.14159'

