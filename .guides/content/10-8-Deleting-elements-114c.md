-----------------

There are several ways to delete elements from a list. If you know the index of the element you want, you can use <span>pop</span>:

    >>> t = ['a', 'b', 'c']
    >>> x = t.pop(1)
    >>> t
    ['a', 'c']
    >>> x
    'b'

<span>`pop`</span> modifies the list and returns the element that was removed. If you don’t provide an index, it deletes and returns the last element.

If you don’t need the removed value, you can use the <span>`del`</span> operator:

    >>> t = ['a', 'b', 'c']
    >>> del t[1]
    >>> t
    ['a', 'c']

If you know the element you want to remove (but not the index), you can use <span>`remove`</span>:

    >>> t = ['a', 'b', 'c']
    >>> t.remove('b')
    >>> t
    ['a', 'c']

The return value from <span>remove</span> is <span>None</span>.

To remove more than one element, you can use <span>del</span> with a slice index:

    >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> del t[1:5]
    >>> t
    ['a', 'f']

As usual, the slice selects all the elements up to but not including the second index.

