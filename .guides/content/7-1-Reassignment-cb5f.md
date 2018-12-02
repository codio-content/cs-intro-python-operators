------------

As you may have discovered, it is legal to make more than one assignment to the same variable. A new assignment makes an existing variable refer to a new value (and stop referring to the old value).

    >>> x = 5
    >>> x
    5
    >>> x = 7
    >>> x
    7

The first time we display <span>x</span>, its value is 5; the second time, its value is 7.

The figure below shows what <span>**reassignment**</span> looks like in a state diagram.

![image](/.guides/img/assign2.jpg)

At this point I want to address a common source of confusion. Because Python uses the equal sign (<span>=</span>) for assignment, it is tempting to interpret a statement like <span>a = b</span> as a mathematical proposition of equality; that is, the claim that <span>a</span> and <span>b</span> are equal. But this interpretation is wrong.

First, equality is a symmetric relationship and assignment is not. For example, in mathematics, if $a=7$ then $7=a$. But in Python, the statement <span>a = 7</span> is legal and <span>7 = a</span> is not.

Also, in mathematics, a proposition of equality is either true or false for all time. If $a=b$ now, then $a$ will always equal $b$. In Python, an assignment statement can make two variables equal, but they don’t have to stay that way:

    >>> a = 5
    >>> b = a    # a and b are now equal
    >>> a = 3    # a and b are no longer equal
    >>> b
    5

The third line changes the value of <span>a</span> but does not change the value of <span>b</span>, so they are no longer equal.

Reassigning variables is often useful, but you should use it with caution. If the values of variables change frequently, it can make the code difficult to read and debug.





