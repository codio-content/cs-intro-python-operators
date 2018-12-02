--------------------------

Rewriting `is_after` (from Section [isafter]) is slightly more complicated because it takes two Time objects as parameters. In this case it is conventional to name the first parameter <span>self</span> and the second parameter <span>other</span>:

    # inside class Time:

        def is_after(self, other):
            return self.time_to_int() > other.time_to_int()

To use this method, you have to invoke it on one object and pass the other as an argument:

    >>> end.is_after(start)
    True

One nice thing about this syntax is that it almost reads like English: “end is after start?”

