-----------------------

Strictly speaking, a function can only return one value, but if the value is a tuple, the effect is the same as returning multiple values. For example, if you want to divide two integers and compute the quotient and remainder, it is inefficient to compute <span>x//y</span> and then <span>x%y</span>. It is better to compute them both at the same time.

The built-in function <span>divmod</span> takes two arguments and returns a tuple of two values, the quotient and remainder. You can store the result as a tuple:

    >>> t = divmod(7, 3)
    >>> t
    (2, 1)

Or use tuple assignment to store the elements separately:

    >>> quot, rem = divmod(7, 3)
    >>> quot
    2
    >>> rem
    1

Here is an example of a function that returns a tuple:

    def min_max(t):
        return min(t), max(t)

<span>max</span> and <span>min</span> are built-in functions that find the largest and smallest elements of a sequence. `min_max` computes both and returns a tuple of two values.

