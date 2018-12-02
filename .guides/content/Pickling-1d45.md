--------

A limitation of <span>dbm</span> is that the keys and values have to be strings or bytes. If you try to use any other type, you get an error.

The <span>pickle</span> module can help. It translates almost any type of object into a string suitable for storage in a database, and then translates strings back into objects.

<span>pickle.dumps</span> takes an object as a parameter and returns a string representation (<span>dumps</span> is short for “dump string”):

    >>> import pickle
    >>> t = [1, 2, 3]
    >>> pickle.dumps(t)
    b'\x80\x03]q\x00(K\x01K\x02K\x03e.'

The format isn’t obvious to human readers; it is meant to be easy for <span>pickle</span> to interpret. <span>pickle.loads</span> (“load string”) reconstitutes the object:

    >>> t1 = [1, 2, 3]
    >>> s = pickle.dumps(t1)
    >>> t2 = pickle.loads(s)
    >>> t2
    [1, 2, 3]

Although the new object has the same value as the old, it is not (in general) the same object:

    >>> t1 == t2
    True
    >>> t1 is t2
    False

In other words, pickling and then unpickling has the same effect as copying the object.

You can use <span>pickle</span> to store non-strings in a database. In fact, this combination is so common that it has been encapsulated in a module called <span>shelve</span>.

