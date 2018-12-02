--------------------

After “Hello, World”, the next step is arithmetic. Python provides <span>**operators**</span>, which are special symbols that represent computations like addition and multiplication.

The operators <span>+</span>, <span>-</span>, and <span>*</span> perform addition, subtraction, and multiplication, as in the following examples:

    >>> 40 + 2
    42
    >>> 43 - 1
    42
    >>> 6 * 7
    42

The operator <span>/</span> performs division:

    >>> 84 / 2
    42.0

You might wonder why the result is <span>42.0</span> instead of <span>42</span>. I’ll explain in the next section.

Finally, the operator <span>\**</span> performs exponentiation; that is, it raises a number to a power:

    >>> 6**2 + 6
    42


In some other languages, `^` is used for exponentiation, but in Python it is a bitwise operator called XOR. If you are not familiar with bitwise operators, the result will surprise you:

    >>> 6 ^ 2
    4

I won’t cover bitwise operators in this book, but you can read about them at <http://wiki.python.org/moin/BitwiseOperators>.

