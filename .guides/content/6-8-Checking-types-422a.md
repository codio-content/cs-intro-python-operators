--------------

What happens if we call <span>factorial</span> and give it 1.5 as an argument?

    >>> factorial(1.5)
    RuntimeError: Maximum recursion depth exceeded

It looks like an infinite recursion. How can that be? The function has a base case—when <span>n == 0</span>. But if <span>n</span> is not an integer, we can <span>*miss*</span> the base case and recurse forever.

In the first recursive call, the value of <span>n</span> is 0.5. In the next, it is -0.5. From there, it gets smaller (more negative), but it will never be 0.

We have two choices. We can try to generalize the <span>factorial</span> function to work with floating-point numbers, or we can make <span>factorial</span> check the type of its argument. The first option is called the gamma function and it’s a little beyond the scope of this book. So we’ll go for the second.

We can use the built-in function <span>isinstance</span> to verify the type of the argument. While we’re at it, we can also make sure the argument is positive:

    def factorial(n):
        if not isinstance(n, int):
            print('Factorial is only defined for integers.')
            return None
        elif n < 0:
            print('Factorial is not defined for negative integers.')
            return None
        elif n == 0:
            return 1
        else:
            return n * factorial(n-1)

The first base case handles nonintegers; the second handles negative integers. In both cases, the program prints an error message and returns <span>None</span> to indicate that something went wrong:

    >>> print(factorial('fred'))
    Factorial is only defined for integers.
    None
    >>> print(factorial(-2))
    Factorial is not defined for negative integers.
    None

If we get past both checks, we know that $n$ is positive or zero, so we can prove that the recursion terminates.

This program demonstrates a pattern sometimes called a <span>**guardian**</span>. The first two conditionals act as guardians, protecting the code that follows from values that might cause an error. The guardians make it possible to prove the correctness of the code.

In Section 11.4 we will see a more flexible alternative to printing an error message: raising an exception.

