------------

Loops are often used in programs that compute numerical results by starting with an approximate answer and iteratively improving it.

For example, one way of computing square roots is Newton’s method. Suppose that you want to know the square root of $a$. If you start with almost any estimate, $x$, you can compute a better estimate with the following formula:

$$y = \frac{x + a/x}{2}$$ For example, if $a$ is 4 and $x$ is 3:

    >>> a = 4
    >>> x = 3
    >>> y = (x + a/x) / 2
    >>> y
    2.16666666667

The result is closer to the correct answer ($\sqrt{4} = 2$). If we repeat the process with the new estimate, it gets even closer:

    >>> x = y
    >>> y = (x + a/x) / 2
    >>> y
    2.00641025641

After a few more updates, the estimate is almost exact:

    >>> x = y
    >>> y = (x + a/x) / 2
    >>> y
    2.00001024003
    >>> x = y
    >>> y = (x + a/x) / 2
    >>> y
    2.00000000003

In general we don’t know ahead of time how many steps it takes to get to the right answer, but we know when we get there because the estimate stops changing:

    >>> x = y
    >>> y = (x + a/x) / 2
    >>> y
    2.0
    >>> x = y
    >>> y = (x + a/x) / 2
    >>> y
    2.0

When <span>y == x</span>, we can stop. Here is a loop that starts with an initial estimate, <span>x</span>, and improves it until it stops changing:

    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y

For most values of <span>a</span> this works fine, but in general it is dangerous to test <span>float</span> equality. Floating-point values are only approximately right: most rational numbers, like $1/3$, and irrational numbers, like $\sqrt{2}$, can’t be represented exactly with a <span>float</span>.

Rather than checking whether <span>x</span> and <span>y</span> are exactly equal, it is safer to use the built-in function <span>abs</span> to compute the absolute value, or magnitude, of the difference between them:

        if abs(y-x) < epsilon:
            break

Where `epsilon` has a value like <span>0.0000001</span> that determines how close is close enough.

