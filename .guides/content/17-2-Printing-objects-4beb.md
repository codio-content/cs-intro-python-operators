----------------

In Chapter 16, we defined a class named <span>Time</span> and in Section 16.1, you wrote a function named `print_time`:

    class Time:
        """Represents the time of day."""

    def print_time(time):
        print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

To call this function, you have to pass a <span>Time</span> object as an argument:

    >>> start = Time()
    >>> start.hour = 9
    >>> start.minute = 45
    >>> start.second = 00
    >>> print_time(start)
    09:45:00

To make `print_time` a method, all we have to do is move the function definition inside the class definition. Notice the change in indentation.

    class Time:
        def print_time(time):
            print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

Now there are two ways to call `print_time`. The first (and less common) way is to use function syntax:

    >>> Time.print_time(start)
    09:45:00

In this use of dot notation, <span>Time</span> is the name of the class, and `print_time` is the name of the method. <span>start</span> is passed as a parameter.

The second (and more concise) way is to use method syntax:

    >>> start.print_time()
    09:45:00

In this use of dot notation, `print_time` is the name of the method (again), and <span>start</span> is the object the method is invoked on, which is called the <span>**subject**</span>. Just as the subject of a sentence is what the sentence is about, the subject of a method invocation is what the method is about.

Inside the method, the subject is assigned to the first parameter, so in this case <span>start</span> is assigned to <span>time</span>.

By convention, the first parameter of a method is called <span>self</span>, so it would be more common to write `print_time` like this:

    class Time:
        def print_time(self):
            print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

The reason for this convention is an implicit metaphor:

-   The syntax for a function call, `print_time(start)`, suggests that the function is the active agent. It says something like, “Hey `print_time`! Here’s an object for you to print.”

-   In object-oriented programming, the objects are the active agents. A method invocation like `start.print_time()` says “Hey <span>start</span>! Please print yourself.”

This change in perspective might be more polite, but it is not obvious that it is useful. In the examples we have seen so far, it may not be. But sometimes shifting responsibility from the functions onto the objects makes it possible to write more versatile functions (or methods), and makes it easier to maintain and reuse code.

As an exercise, rewrite `time_to_int` (from Section 16.4) as a method. You might be tempted to rewrite `int_to_time` as a method, too, but that doesn’t really make sense because there would be no object to invoke it on.

