--------------------------

The <span>**floor division**</span> operator, `//`, divides two numbers and rounds down to an integer. For example, suppose the run time of a movie is 105 minutes. You might want to know how long that is in hours. Conventional division returns a floating-point number:

    >>> minutes = 105
    >>> minutes / 60
    1.75

But we don’t normally write hours with decimal points. Floor division returns the integer number of hours, rounding down:

    >>> minutes = 105
    >>> hours = minutes // 60
    >>> hours
    1

To get the remainder, you could subtract off one hour in minutes:

    >>> remainder = minutes - hours * 60
    >>> remainder
    45

An alternative is to use the <span>**modulus operator**</span>, `%`, which divides two numbers and returns the remainder.

    >>> remainder = minutes % 60
    >>> remainder
    45

The modulus operator is more useful than it seems. For example, you can check whether one number is divisible by another—if <span>x % y</span> is zero, then <span>x</span> is divisible by <span>y</span>.

Also, you can extract the right-most digit or digits from a number. For example, <span>x % 10</span> yields the right-most digit of <span>x</span> (in base 10). Similarly <span>x % 100</span> yields the last two digits.

If you are using Python 2, division works differently. The division operator, `/`, performs floor division if both operands are integers, and floating-point division if either operand is a <span>float</span>.

