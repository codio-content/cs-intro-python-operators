-------------

Calling the function generates a return value, which we usually assign to a variable or use as part of an expression.

    e = math.exp(1.0)
    height = radius * math.sin(radians)

The functions we have written so far are void. Speaking casually, they have no return value; more precisely, their return value is <span>None</span>.

In this chapter, we are (finally) going to write fruitful functions. The first example is <span>area</span>, which returns the area of a circle with the given radius:

    def area(radius):
        a = math.pi * radius**2
        return a

We have seen the <span>return</span> statement before, but in a fruitful function the <span>return</span> statement includes an expression. This statement means: “Return immediately from this function and use the following expression as a return value.” The expression can be arbitrarily complicated, so we could have written this function more concisely:

    def area(radius):
        return math.pi * radius**2

On the other hand, <span>**temporary variables**</span> like <span>a</span> can make debugging easier.

Sometimes it is useful to have multiple return statements, one in each branch of a conditional:

    def absolute_value(x):
        if x < 0:
            return -x
        else:
            return x

Since these <span>return</span> statements are in an alternative conditional, only one runs.

As soon as a return statement runs, the function terminates without executing any subsequent statements. Code that appears after a <span>return</span> statement, or any other place the flow of execution can never reach, is called <span>**dead code**</span>.

In a fruitful function, it is a good idea to ensure that every possible path through the program hits a <span>return</span> statement. For example:

    def absolute_value(x):
        if x < 0:
            return -x
        if x > 0:
            return x

This function is incorrect because if <span>x</span> happens to be 0, neither condition is true, and the function ends without hitting a <span>return</span> statement. If the flow of execution gets to the end of a function, the return value is <span>None</span>, which is not the absolute value of 0.

    >>> print(absolute_value(0))
    None

By the way, Python provides a built-in function called <span>abs</span> that computes absolute values.

As an exercise, write a <span>compare</span> function takes two values, <span>x</span> and <span>y</span>, and returns <span>1</span> if <span>x \> y</span>, <span>0</span> if <span>x == y</span>, and <span>-1</span> if <span>x \< y</span>.


{ Try it }(sh .guides/bg.sh python3 code/return_values.py)

