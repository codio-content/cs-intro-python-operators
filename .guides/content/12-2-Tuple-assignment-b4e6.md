----------------

It is often useful to swap the values of two variables. With conventional assignments, you have to use a temporary variable. For example, to swap <span>a</span> and <span>b</span>:

    >>> temp = a
    >>> a = b
    >>> b = temp

This solution is cumbersome; <span>**tuple assignment**</span> is more elegant:

    >>> a, b = b, a

The left side is a tuple of variables; the right side is a tuple of expressions. Each value is assigned to its respective variable. All the expressions on the right side are evaluated before any of the assignments.

The number of variables on the left and the number of values on the right have to be the same:

    >>> a, b = 1, 2, 3
    ValueError: too many values to unpack

More generally, the right side can be any kind of sequence (string, list or tuple). For example, to split an email address into a user name and a domain, you could write:

    >>> addr = 'monty@python.org'
    >>> uname, domain = addr.split('@')

The return value from <span>split</span> is a list with two elements; the first element is assigned to <span>uname</span>, the second to <span>domain</span>.

    >>> uname
    'monty'
    >>> domain
    'python.org'

