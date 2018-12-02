---------------

The init method (short for “initialization”) is a special method that gets invoked when an object is instantiated. Its full name is `__init__` (two underscore characters, followed by <span>init</span>, and then two more underscores). An init method for the <span>Time</span> class might look like this:

    # inside class Time:

        def __init__(self, hour=0, minute=0, second=0):
            self.hour = hour
            self.minute = minute
            self.second = second

It is common for the parameters of `__init__` to have the same names as the attributes. The statement

            self.hour = hour

stores the value of the parameter <span>hour</span> as an attribute of <span>self</span>.

The parameters are optional, so if you call <span>Time</span> with no arguments, you get the default values.

    >>> time = Time()
    >>> time.print_time()
    00:00:00

If you provide one argument, it overrides <span>hour</span>:

    >>> time = Time (9)
    >>> time.print_time()
    09:00:00

If you provide two arguments, they override <span>hour</span> and <span>minute</span>.

    >>> time = Time(9, 45)
    >>> time.print_time()
    09:45:00

And if you provide three arguments, they override all three default values.

As an exercise, write an init method for the <span>Point</span> class that takes <span>x</span> and <span>y</span> as optional parameters and assigns them to the corresponding attributes.

