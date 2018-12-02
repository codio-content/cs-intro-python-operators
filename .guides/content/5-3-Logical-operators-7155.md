-----------------

There are three <span>**logical operators**</span>: <span>and</span>, <span>or</span>, and <span>not</span>. The semantics (meaning) of these operators is similar to their meaning in English. For example, <span>x \> 0 and x \< 10</span> is true only if <span>x</span> is greater than 0 <span>*and*</span> less than 10.

<span>n%2 == 0 or n%3 == 0</span> is true if <span>*either or both*</span> of the conditions is true, that is, if the number is divisible by 2 <span>*or*</span> 3.

Finally, the <span>not</span> operator negates a boolean expression, so <span>not (x \> y)</span> is true if <span>x \> y</span> is false, that is, if <span>x</span> is less than or equal to <span>y</span>.

Strictly speaking, the operands of the logical operators should be boolean expressions, but Python is not very strict. Any nonzero number is interpreted as <span>True</span>:

    >>> 42 and True
    True

This flexibility can be useful, but there are some subtleties to it that might be confusing. You might want to avoid it (unless you know what you are doing).

