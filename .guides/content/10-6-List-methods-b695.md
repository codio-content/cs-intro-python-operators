------------

Python provides methods that operate on lists. For example, <span>append</span> adds a new element to the end of a list:

    >>> t = ['a', 'b', 'c']
    >>> t.append('d')
    >>> t
    ['a', 'b', 'c', 'd']

<span>`extend`</span> takes a list as an argument and appends all of the elements:

    >>> t1 = ['a', 'b', 'c']
    >>> t2 = ['d', 'e']
    >>> t1.extend(t2)
    >>> t1
    ['a', 'b', 'c', 'd', 'e']

This example leaves <span>t2</span> unmodified.

<span>`sort`</span> arranges the elements of the list from low to high:

    >>> t = ['d', 'c', 'e', 'b', 'a']
    >>> t.sort()
    >>> t
    ['a', 'b', 'c', 'd', 'e']

Most list methods are void; they modify the list and return <span>None</span>. If you accidentally write <span>`t = t.sort()`</span>, you will be disappointed with the result.

