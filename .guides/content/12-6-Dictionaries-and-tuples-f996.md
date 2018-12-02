-----------------------

Dictionaries have a method called <span>items</span> that returns a sequence of tuples, where each tuple is a key-value pair.

    >>> d = {'a':0, 'b':1, 'c':2}
    >>> t = d.items()
    >>> t
    dict_items([('c', 2), ('a', 0), ('b', 1)])

The result is a `dict_items` object, which is an iterator that iterates the key-value pairs. You can use it in a <span>for</span> loop like this:

    >>> for key, value in d.items():
    ...     print(key, value)
    ...
    c 2
    a 0
    b 1

As you should expect from a dictionary, the items are in no particular order.

Going in the other direction, you can use a list of tuples to initialize a new dictionary:

    >>> t = [('a', 0), ('c', 2), ('b', 1)]
    >>> d = dict(t)
    >>> d
    {'a': 0, 'c': 2, 'b': 1}

Combining <span>dict</span> with <span>zip</span> yields a concise way to create a dictionary:

    >>> d = dict(zip('abc', range(3)))
    >>> d
    {'a': 0, 'c': 2, 'b': 1}

The dictionary method <span>update</span> also takes a list of tuples and adds them, as key-value pairs, to an existing dictionary.

It is common to use tuples as keys in dictionaries (primarily because you can’t use lists). For example, a telephone directory might map from last-name, first-name pairs to telephone numbers. Assuming that we have defined <span>last</span>, <span>first</span> and <span>number</span>, we could write:

    directory[last, first] = number

The expression in brackets is a tuple. We could use tuple assignment to traverse this dictionary.

    for last, first in directory:
        print(first, last, directory[last,first])

This loop traverses the keys in <span>directory</span>, which are tuples. It assigns the elements of each tuple to <span>last</span> and <span>first</span>, then prints the name and corresponding telephone number.

There are two ways to represent tuples in a state diagram. The more detailed version shows the indices and elements just as they appear in a list. For example, the tuple `('Cleese', 'John')` would appear as in Figure .

![image](/.guides/img/tuple1.jpg)



But in a larger diagram you might want to leave out the details. For example, a diagram of the telephone directory might appear as in Figure .

![image](/.guides/img/dict2.jpg)



Here the tuples are shown using Python syntax as a graphical shorthand. The telephone number in the diagram is the complaints line for the BBC, so please don’t call it.

