-----------------------------------

`__str__` is a special method, like `__init__`, that is supposed to return a string representation of an object.

For example, here is a <span>str</span> method for Time objects:

    # inside class Time:

        def __str__(self):
            return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

When you <span>print</span> an object, Python invokes the <span>str</span> method:

    >>> time = Time(9, 45)
    >>> print(time)
    09:45:00

When I write a new class, I almost always start by writing `__init__`, which makes it easier to instantiate objects, and `__str__`, which is useful for debugging.

As an exercise, write a <span>str</span> method for the <span>Point</span> class. Create a Point object and print it.

