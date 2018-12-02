------------

Type-based dispatch is useful when it is necessary, but (fortunately) it is not always necessary. Often you can avoid it by writing functions that work correctly for arguments with different types.

Many of the functions we wrote for strings also work for other sequence types. For example, in Section [histogram] we used <span>histogram</span> to count the number of times each letter appears in a word.

    def histogram(s):
        d = dict()
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c]+1
        return d

This function also works for lists, tuples, and even dictionaries, as long as the elements of <span>s</span> are hashable, so they can be used as keys in <span>d</span>.

    >>> t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
    >>> histogram(t)
    {'bacon': 1, 'egg': 1, 'spam': 4}

Functions that work with several types are called <span>**polymorphic**</span>. Polymorphism can facilitate code reuse. For example, the built-in function <span>sum</span>, which adds the elements of a sequence, works as long as the elements of the sequence support addition.

Since Time objects provide an <span>add</span> method, they work with <span>sum</span>:

    >>> t1 = Time(7, 43)
    >>> t2 = Time(7, 41)
    >>> t3 = Time(7, 37)
    >>> total = sum([t1, t2, t3])
    >>> print(total)
    23:01:00

In general, if all of the operations inside a function work with a given type, the function works with that type.

The best kind of polymorphism is the unintentional kind, where you discover that a function you already wrote can be applied to a type you never planned for.

