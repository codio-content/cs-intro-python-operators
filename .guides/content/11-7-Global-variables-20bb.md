----------------

In the previous example, <span>known</span> is created outside the function, so it belongs to the special frame called `__main__`. Variables in `__main__` are sometimes called <span>**global**</span> because they can be accessed from any function. Unlike local variables, which disappear when their function ends, global variables persist from one function call to the next.

It is common to use global variables for <span>**flags**</span>; that is, boolean variables that indicate (“flag”) whether a condition is true. For example, some programs use a flag named <span>verbose</span> to control the level of detail in the output:

    verbose = True

    def example1():
        if verbose:
            print('Running example1')

If you try to reassign a global variable, you might be surprised. The following example is supposed to keep track of whether the function has been called:

    been_called = False

    def example2():
        been_called = True         # WRONG

But if you run it you will see that the value of `been_called` doesn’t change. The problem is that <span>example2</span> creates a new local variable named `been_called`. The local variable goes away when the function ends, and has no effect on the global variable.

To reassign a global variable inside a function you have to <span>**declare**</span> the global variable before you use it:

    been_called = False

    def example2():
        global been_called 
        been_called = True

The <span>**global statement**</span> tells the interpreter something like, “In this function, when I say `been_called`, I mean the global variable; don’t create a local one.”

Here’s an example that tries to update a global variable:

    count = 0

    def example3():
        count = count + 1          # WRONG

If you run it you get:

    UnboundLocalError: local variable 'count' referenced before assignment

Python assumes that <span>count</span> is local, and under that assumption you are reading it before writing it. The solution, again, is to declare <span>count</span> global.

    def example3():
        global count
        count += 1

If a global variable refers to a mutable value, you can modify the value without declaring the variable:

    known = {0:0, 1:1}

    def example4():
        known[2] = 1

So you can add, remove and replace elements of a global list or dictionary, but if you want to reassign the variable, you have to declare it:

    def example5():
        global known
        known = dict()

Global variables can be useful, but if you have a lot of them, and you modify them frequently, they can make programs hard to debug.

