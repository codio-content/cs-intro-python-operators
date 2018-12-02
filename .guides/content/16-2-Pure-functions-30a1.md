--------------

In the next few sections, we’ll write two functions that add time values. They demonstrate two kinds of functions: pure functions and modifiers. They also demonstrate a development plan I’ll call <span>**prototype and patch**</span>, which is a way of tackling a complex problem by starting with a simple prototype and incrementally dealing with the complications.

Here is a simple prototype of `add_time`:

    def add_time(t1, t2):
        sum = Time()
        sum.hour = t1.hour + t2.hour
        sum.minute = t1.minute + t2.minute
        sum.second = t1.second + t2.second
        return sum

The function creates a new <span>Time</span> object, initializes its attributes, and returns a reference to the new object. This is called a <span>**pure function**</span> because it does not modify any of the objects passed to it as arguments and it has no effect, like displaying a value or getting user input, other than returning a value.

To test this function, I’ll create two Time objects: <span>start</span> contains the start time of a movie, like <span>*Monty Python and the Holy Grail*</span>, and <span>duration</span> contains the run time of the movie, which is one hour 35 minutes.

`add_time` figures out when the movie will be done.

    >>> start = Time()
    >>> start.hour = 9
    >>> start.minute = 45
    >>> start.second =  0

    >>> duration = Time()
    >>> duration.hour = 1
    >>> duration.minute = 35
    >>> duration.second = 0

    >>> done = add_time(start, duration)
    >>> print_time(done)
    10:80:00

The result, <span>10:80:00</span> might not be what you were hoping for. The problem is that this function does not deal with cases where the number of seconds or minutes adds up to more than sixty. When that happens, we have to “carry” the extra seconds into the minute column or the extra minutes into the hour column.

Here’s an improved version:

    def add_time(t1, t2):
        sum = Time()
        sum.hour = t1.hour + t2.hour
        sum.minute = t1.minute + t2.minute
        sum.second = t1.second + t2.second

        if sum.second >= 60:
            sum.second -= 60
            sum.minute += 1

        if sum.minute >= 60:
            sum.minute -= 60
            sum.hour += 1

        return sum

Although this function is correct, it is starting to get big. We will see a shorter alternative later.

