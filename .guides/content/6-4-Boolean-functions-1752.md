-----------------

Functions can return booleans, which is often convenient for hiding complicated tests inside functions. For example:

    def is_divisible(x, y):
        if x % y == 0:
            return True
        else:
            return False

It is common to give boolean functions names that sound like yes/no questions; `is_divisible` returns either <span>True</span> or <span>False</span> to indicate whether <span>x</span> is divisible by <span>y</span>.

Here is an example:

    >>> is_divisible(6, 4)
    False
    >>> is_divisible(6, 3)
    True

The result of the <span>==</span> operator is a boolean, so we can write the function more concisely by returning it directly:

    def is_divisible(x, y):
        return x % y == 0

Boolean functions are often used in conditional statements:

    if is_divisible(x, y):
        print('x is divisible by y')

It might be tempting to write something like:

    if is_divisible(x, y) == True:
        print('x is divisible by y')

But the extra comparison is unnecessary.

As an exercise, write a function `is_between(x, y, z)` that returns <span>True</span> if $x \le y \le z$ or <span>False</span> otherwise.

