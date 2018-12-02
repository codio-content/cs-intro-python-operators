---------

When a syntax or runtime error occurs, the error message contains a lot of information, but it can be overwhelming. The most useful parts are usually:

-   What kind of error it was, and

-   Where it occurred.

Syntax errors are usually easy to find, but there are a few gotchas. Whitespace errors can be tricky because spaces and tabs are invisible and we are used to ignoring them.

    >>> x = 5
    >>>  y = 6
      File "<stdin>", line 1
        y = 6
        ^
    IndentationError: unexpected indent

In this example, the problem is that the second line is indented by one space. But the error message points to <span>y</span>, which is misleading. In general, error messages indicate where the problem was discovered, but the actual error might be earlier in the code, sometimes on a previous line.

The same is true of runtime errors. Suppose you are trying to compute a signal-to-noise ratio in decibels. The formula is $SNR_{db} = 10 \log_{10} (P_{signal} / P_{noise})$. In Python, you might write something like this:

    import math
    signal_power = 9
    noise_power = 10
    ratio = signal_power // noise_power
    decibels = 10 * math.log10(ratio)
    print(decibels)

When you run this program, you get an exception:

    Traceback (most recent call last):
      File "snr.py", line 5, in ?
        decibels = 10 * math.log10(ratio)
    ValueError: math domain error

The error message indicates line 5, but there is nothing wrong with that line. To find the real error, it might be useful to print the value of <span>ratio</span>, which turns out to be 0. The problem is in line 4, which uses floor division instead of floating-point division.

You should take the time to read error messages carefully, but don’t assume that everything they say is correct.

