--------------

When you pass a list to a function, the function gets a reference to the list. If the function modifies the list, the caller sees the change. For example, `delete_head` removes the first element from a list:

    def delete_head(t):
        del t[0]

Here’s how it is used:

    >>> letters = ['a', 'b', 'c']
    >>> delete_head(letters)
    >>> letters
    ['b', 'c']

The parameter <span>t</span> and the variable <span>letters</span> are aliases for the same object. The stack diagram looks like the Figure below.

![image](/.guides/img/stack5.jpg)



Since the list is shared by two frames, I drew it between them.

It is important to distinguish between operations that modify lists and operations that create new lists. For example, the <span>`append`</span> method modifies a list, but the <span>+</span> operator creates a new list.

Here’s an example using <span>append</span>:

    >>> t1 = [1, 2]
    >>> t2 = t1.append(3)
    >>> t1
    [1, 2, 3]
    >>> t2
    None

The return value from <span>append</span> is <span>None</span>.

Here’s an example using the <span>+</span> operator:

    >>> t3 = t1 + [4]
    >>> t1
    [1, 2, 3]
    >>> t3
    [1, 2, 3, 4]

The result of the operator is a new list, and the original list is unchanged.

This difference is important when you write functions that are supposed to modify lists. For example, this function <span>*does not*</span> delete the head of a list:

    def bad_delete_head(t):
        t = t[1:]              # WRONG!

The slice operator creates a new list and the assignment makes <span>t</span> refer to it, but that doesn’t affect the caller.

    >>> t4 = [1, 2, 3]
    >>> bad_delete_head(t4)
    >>> t4
    [1, 2, 3]

At the beginning of `bad_delete_head`, <span>t</span> and <span>t4</span> refer to the same list. At the end, <span>t</span> refers to a new list, but <span>t4</span> still refers to the original, unmodified list.

An alternative is to write a function that creates and returns a new list. For example, <span>`tail`</span> returns all but the first element of a list:

    def tail(t):
        return t[1:]

This function leaves the original list unmodified. Here’s how it is used:

    >>> letters = ['a', 'b', 'c']
    >>> rest = tail(letters)
    >>> rest
    ['b', 'c']

