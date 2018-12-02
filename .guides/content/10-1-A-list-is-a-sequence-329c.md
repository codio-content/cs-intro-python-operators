--------------------

Like a string, a <span>**list**</span> is a sequence of values. In a string, the values are characters; in a list, they can be any type. The values in a list are called <span>**elements**</span> or sometimes <span>**items**</span>.

There are several ways to create a new list; the simplest is to enclose the elements in square brackets (`[` and `]`):

    [10, 20, 30, 40]
    ['crunchy frog', 'ram bladder', 'lark vomit']

The first example is a list of four integers. The second is a list of three strings. The elements of a list don’t have to be the same type. The following list contains a string, a float, an integer, and (lo!) another list:

    ['spam', 2.0, 5, [10, 20]]

A list within another list is <span>**nested**</span>.

A list that contains no elements is called an empty list; you can create one with empty brackets, `[]`.

As you might expect, you can assign list values to variables:

    >>> cheeses = ['Cheddar', 'Edam', 'Gouda']
    >>> numbers = [42, 123]
    >>> empty = []
    >>> print(cheeses, numbers, empty)
    ['Cheddar', 'Edam', 'Gouda'] [42, 123] []

