---------

Sometimes it is useful for a function to modify the objects it gets as parameters. In that case, the changes are visible to the caller. Functions that work this way are called <span>**modifiers**</span>.

<span>`increment`</span>, which adds a given number of seconds to a <span>Time</span> object, can be written naturally as a modifier. Here is a rough draft:

    def increment(time, seconds):
        time.second += seconds

        if time.second >= 60:
            time.second -= 60
            time.minute += 1

        if time.minute >= 60:
            time.minute -= 60
            time.hour += 1

The first line performs the basic operation; the remainder deals with the special cases we saw before.

Is this function correct? What happens if <span>seconds</span> is much greater than sixty?

In that case, it is not enough to carry once; we have to keep doing it until <span>time.second</span> is less than sixty. One solution is to replace the <span>if</span> statements with <span>while</span> statements. That would make the function correct, but not very efficient. As an exercise, write a correct version of <span>increment</span> that doesn’t contain any loops.

Anything that can be done with modifiers can also be done with pure functions. In fact, some programming languages only allow pure functions. There is some evidence that programs that use pure functions are faster to develop and less error-prone than programs that use modifiers. But modifiers are convenient at times, and functional programs tend to be less efficient.

In general, I recommend that you write pure functions whenever it is reasonable and resort to modifiers only if there is a compelling advantage. This approach might be called a <span>**functional programming style**</span>.

As an exercise, write a “pure” version of <span>increment</span> that creates and returns a new Time object rather than modifying the parameter.

