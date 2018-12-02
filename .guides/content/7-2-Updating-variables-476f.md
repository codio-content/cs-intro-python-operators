------------------

A common kind of reassignment is an <span>**update**</span>, where the new value of the variable depends on the old.

    >>> x = x + 1

This means “get the current value of <span>x</span>, add one, and then update <span>x</span> with the new value.”

If you try to update a variable that doesn’t exist, you get an error, because Python evaluates the right side before it assigns a value to <span>x</span>:

    >>> x = x + 1
    NameError: name 'x' is not defined

Before you can update a variable, you have to <span>**initialize**</span> it, usually with a simple assignment:

    >>> x = 0
    >>> x = x + 1

Updating a variable by adding 1 is called an <span>**increment**</span>; subtracting 1 is called a <span>**decrement**</span>.

