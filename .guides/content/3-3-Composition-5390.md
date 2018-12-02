-----------

So far, we have looked at the elements of a program—variables, expressions, and statements—in isolation, without talking about how to combine them.

One of the most useful features of programming languages is their ability to take small building blocks and <span>**compose**</span> them. For example, the argument of a function can be any kind of expression, including arithmetic operators:

    x = math.sin(degrees / 360.0 * 2 * math.pi)

And even function calls:

    x = math.exp(math.log(x+1))

Almost anywhere you can put a value, you can put an arbitrary expression, with one exception: the left side of an assignment statement has to be a variable name. Any other expression on the left side is a syntax error (we will see exceptions to this rule later).

    >>> minutes = hours * 60                 # right
    >>> hours * 60 = minutes                 # wrong!
    SyntaxError: can't assign to operator

