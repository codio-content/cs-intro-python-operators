--------

If <span>`a`</span> refers to an object and you assign <span>b = a</span>, then both variables refer to the same object:

    >>> a = [1, 2, 3]
    >>> b = a
    >>> b is a
    True

The state diagram looks like the Figure below.

![image](/.guides/img/list3.jpg)



The association of a variable with an object is called a <span>**reference**</span>. In this example, there are two references to the same object.

An object with more than one reference has more than one name, so we say that the object is <span>**aliased**</span>.

If the aliased object is mutable, changes made with one alias affect the other:

    >>> b[0] = 42
    >>> a
    [42, 2, 3]

Although this behavior can be useful, it is error-prone. In general, it is safer to avoid aliasing when you are working with mutable objects.

For immutable objects like strings, aliasing is not as much of a problem. In this example:

    a = 'banana'
    b = 'banana'

It almost never makes a difference whether <span>a</span> and <span>b</span> refer to the same string or not.

