---------

Lists, dictionaries and tuples are examples of <span>**data structures**</span>; in this chapter we are starting to see compound data structures, like lists of tuples, or dictionaries that contain tuples as keys and lists as values. Compound data structures are useful, but they are prone to what I call <span>**shape errors**</span>; that is, errors caused when a data structure has the wrong type, size, or structure. For example, if you are expecting a list with one integer and I give you a plain old integer (not in a list), it won’t work.

To help debug these kinds of errors, I have written a module called <span>`structshape`</span> that provides a function, also called <span>structshape</span>, that takes any kind of data structure as an argument and returns a string that summarizes its shape. You can download it from <http://thinkpython2.com/code/structshape.py>

Here’s the result for a simple list:

    >>> from structshape import structshape
    >>> t = [1, 2, 3]
    >>> structshape(t)
    'list of 3 int'

A fancier program might write “list of 3 int<span>*s*</span>”, but it was easier not to deal with plurals. Here’s a list of lists:

    >>> t2 = [[1,2], [3,4], [5,6]]
    >>> structshape(t2)
    'list of 3 list of 2 int'

If the elements of the list are not the same type, <span>structshape</span> groups them, in order, by type:

    >>> t3 = [1, 2, 3, 4.0, '5', '6', [7], [8], 9]
    >>> structshape(t3)
    'list of (3 int, float, 2 str, 2 list of int, int)'

Here’s a list of tuples:

    >>> s = 'abc'
    >>> lt = list(zip(t, s))
    >>> structshape(lt)
    'list of 3 tuple of (int, str)'

And here’s a dictionary with 3 items that map integers to strings.

    >>> d = dict(lt) 
    >>> structshape(d)
    'dict of 3 int->str'

If you are having trouble keeping track of your data structures, <span>structshape</span> can help.

