----------------

<span>`zip`</span> is a built-in function that takes two or more sequences and returns a list of tuples where each tuple contains one element from each sequence. The name of the function refers to a zipper, which joins and interleaves two rows of teeth.

This example zips a string and a list:

    >>> s = 'abc'
    >>> t = [0, 1, 2]
    >>> zip(s, t)
    <zip object at 0x7f7d0a9e7c48>

The result is a <span>**zip object**</span> that knows how to iterate through the pairs. The most common use of <span>zip</span> is in a <span>for</span> loop:

    >>> for pair in zip(s, t):
    ...     print(pair)
    ...
    ('a', 0)
    ('b', 1)
    ('c', 2)

A zip object is a kind of <span>**iterator**</span>, which is any object that iterates through a sequence. Iterators are similar to lists in some ways, but unlike lists, you can’t use an index to select an element from an iterator.

If you want to use list operators and methods, you can use a zip object to make a list:

    >>> list(zip(s, t))
    [('a', 0), ('b', 1), ('c', 2)]

The result is a list of tuples; in this example, each tuple contains a character from the string and the corresponding element from the list.

If the sequences are not the same length, the result has the length of the shorter one.

    >>> list(zip('Anne', 'Elk'))
    [('A', 'E'), ('n', 'l'), ('n', 'k')]

You can use tuple assignment in a <span>for</span> loop to traverse a list of tuples:

    t = [('a', 0), ('b', 1), ('c', 2)]
    for letter, number in t:
        print(number, letter)

Each time through the loop, Python selects the next tuple in the list and assigns the elements to <span>letter</span> and <span>number</span>. The output of this loop is:

    0 a
    1 b
    2 c

If you combine <span>zip</span>, <span>for</span> and tuple assignment, you get a useful idiom for traversing two (or more) sequences at the same time. For example, `has_match` takes two sequences, <span>t1</span> and <span>t2</span>, and returns <span>True</span> if there is an index <span>i</span> such that <span>t1[i] == t2[i]</span>:

    def has_match(t1, t2):
        for x, y in zip(t1, t2):
            if x == y:
                return True
        return False

If you need to traverse the elements of a sequence and their indices, you can use the built-in function <span>`enumerate`</span>:

    for index, element in enumerate('abc'):
        print(index, element)

The result from <span>enumerate</span> is an enumerate object, which iterates a sequence of pairs; each pair contains an index (starting from 0) and an element from the given sequence. In this example, the output is

    0 a
    1 b
    2 c

Again.

