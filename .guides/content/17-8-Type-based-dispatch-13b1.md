-------------------

In the previous section we added two Time objects, but you also might want to add an integer to a Time object. The following is a version of `__add__` that checks the type of <span>other</span> and invokes either `add_time` or <span>increment</span>:

    # inside class Time:

        def __add__(self, other):
            if isinstance(other, Time):
                return self.add_time(other)
            else:
                return self.increment(other)

        def add_time(self, other):
            seconds = self.time_to_int() + other.time_to_int()
            return int_to_time(seconds)

        def increment(self, seconds):
            seconds += self.time_to_int()
            return int_to_time(seconds)

The built-in function <span>isinstance</span> takes a value and a class object, and returns <span>True</span> if the value is an instance of the class.

If <span>other</span> is a Time object, `__add__` invokes `add_time`. Otherwise it assumes that the parameter is a number and invokes <span>increment</span>. This operation is called a <span>**type-based dispatch**</span> because it dispatches the computation to different methods based on the type of the arguments.

Here are examples that use the <span>+</span> operator with different types:

    >>> start = Time(9, 45)
    >>> duration = Time(1, 35)
    >>> print(start + duration)
    11:20:00
    >>> print(start + 1337)
    10:07:17

Unfortunately, this implementation of addition is not commutative. If the integer is the first operand, you get

    >>> print(1337 + start)
    TypeError: unsupported operand type(s) for +: 'int' and 'instance'

The problem is, instead of asking the Time object to add an integer, Python is asking an integer to add a Time object, and it doesn’t know how. But there is a clever solution for this problem: the special method `__radd__`, which stands for “right-side add”. This method is invoked when a Time object appears on the right side of the <span>+</span> operator. Here’s the definition:

    # inside class Time:

        def __radd__(self, other):
            return self.__add__(other)

And here’s how it’s used:

    >>> print(1337 + start)
    10:07:17

As an exercise, write an <span>add</span> method for Points that works with either a Point object or a tuple:

-   If the second operand is a Point, the method should return a new Point whose $x$ coordinate is the sum of the $x$ coordinates of the operands, and likewise for the $y$ coordinates.

-   If the second operand is a tuple, the method should add the first element of the tuple to the $x$ coordinate and the second element to the $y$ coordinate, and return a new Point with the result.

