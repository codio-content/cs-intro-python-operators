---------

It is legal for one function to call another; it is also legal for a function to call itself. It may not be obvious why that is a good thing, but it turns out to be one of the most magical things a program can do. For example, look at the following function:

    def countdown(n):
        if n <= 0:
            print('Blastoff!')
        else:
            print(n)
            countdown(n-1)

If <span>n</span> is 0 or negative, it outputs the word, “Blastoff!” Otherwise, it outputs <span>n</span> and then calls a function named <span>countdown</span>—itself—passing <span>n-1</span> as an argument.

What happens if we call this function like this?

    >>> countdown(3)

The execution of <span>countdown</span> begins with <span>n=3</span>, and since <span>n</span> is greater than 0, it outputs the value 3, and then calls itself...

> The execution of <span>countdown</span> begins with <span>n=2</span>, and since <span>n</span> is greater than 0, it outputs the value 2, and then calls itself...
>
> > The execution of <span>countdown</span> begins with <span>n=1</span>, and since <span>n</span> is greater than 0, it outputs the value 1, and then calls itself...
> >
> > > The execution of <span>countdown</span> begins with <span>n=0</span>, and since <span>n</span> is not greater than 0, it outputs the word, “Blastoff!” and then returns.
> >
> > The <span>countdown</span> that got <span>n=1</span> returns.
>
> The <span>countdown</span> that got <span>n=2</span> returns.

The <span>countdown</span> that got <span>n=3</span> returns.

And then you’re back in `__main__`. So, the total output looks like this:

    3
    2
    1
    Blastoff!

A function that calls itself is <span>**recursive**</span>; the process of executing it is called <span>**recursion**</span>.

As another example, we can write a function that prints a string <span>n</span> times.

    def print_n(s, n):
        if n <= 0:
            return
        print(s)
        print_n(s, n-1)

If <span>n \<= 0</span> the <span>**return statement**</span> exits the function. The flow of execution immediately returns to the caller, and the remaining lines of the function don’t run.

The rest of the function is similar to <span>countdown</span>: it displays <span>s</span> and then calls itself to display <span>s</span> $n-1$ additional times. So the number of lines of output is <span>1 + (n - 1)</span>, which adds up to <span>n</span>.

For simple examples like this, it is probably easier to use a <span>for</span> loop. But we will see examples later that are hard to write with a <span>for</span> loop and easy to write with recursion, so it is good to start early.

