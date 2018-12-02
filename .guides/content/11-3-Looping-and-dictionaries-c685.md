------------------------

If you use a dictionary in a <span>for</span> statement, it traverses the keys of the dictionary. For example, `print_hist` prints each key and the corresponding value:

    def print_hist(h):
        for c in h:
            print(c, h[c])

Here’s what the output looks like:

    >>> h = histogram('parrot')
    >>> print_hist(h)
    a 1
    p 1
    r 2
    t 1
    o 1

Again, the keys are in no particular order. To traverse the keys in sorted order, you can use the built-in function <span>`sorted`</span>:

    >>> for key in sorted(h):
    ...     print(key, h[key])
    a 1
    o 1
    p 1
    r 2
    t 1

