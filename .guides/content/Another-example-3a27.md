---------------

Here’s a version of <span>increment</span> (from Section [increment]) rewritten as a method:

    # inside class Time:

        def increment(self, seconds):
            seconds += self.time_to_int()
            return int_to_time(seconds)

This version assumes that `time_to_int` is written as a method. Also, note that it is a pure function, not a modifier.

Here’s how you would invoke <span>increment</span>:

    >>> start.print_time()
    09:45:00
    >>> end = start.increment(1337)
    >>> end.print_time()
    10:07:17

The subject, <span>start</span>, gets assigned to the first parameter, <span>self</span>. The argument, <span>1337</span>, gets assigned to the second parameter, <span>seconds</span>.

This mechanism can be confusing, especially if you make an error. For example, if you invoke <span>increment</span> with two arguments, you get:

    >>> end = start.increment(1337, 460)
    TypeError: increment() takes 2 positional arguments but 3 were given

The error message is initially confusing, because there are only two arguments in parentheses. But the subject is also considered an argument, so all together that’s three.

By the way, a <span>**positional argument**</span> is an argument that doesn’t have a parameter name; that is, it is not a keyword argument. In this function call:

    sketch(parrot, cage, dead=True)

<span>parrot</span> and <span>cage</span> are positional, and <span>dead</span> is a keyword argument.

