--------------------

By defining other special methods, you can specify the behavior of operators on programmer-defined types. For example, if you define a method named `__add__` for the <span>Time</span> class, you can use the <span>+</span> operator on Time objects.

Here is what the definition might look like:

    # inside class Time:

        def __add__(self, other):
            seconds = self.time_to_int() + other.time_to_int()
            return int_to_time(seconds)

And here is how you could use it:

    >>> start = Time(9, 45)
    >>> duration = Time(1, 35)
    >>> print(start + duration)
    11:20:00

When you apply the <span>+</span> operator to Time objects, Python invokes `__add__`. When you print the result, Python invokes `__str__`. So there is a lot happening behind the scenes!

Changing the behavior of an operator so that it works with programmer-defined types is called <span>**operator overloading**</span>. For every operator in Python there is a corresponding special method, like `__add__`. For more details, see <http://docs.python.org/3/reference/datamodel.html#specialnames>.

As an exercise, write an <span>add</span> method for the Point class.

