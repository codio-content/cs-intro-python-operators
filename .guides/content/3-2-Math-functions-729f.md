--------------

Python has a math module that provides most of the familiar mathematical functions. A <span>**module**</span> is a file that contains a collection of related functions.

Before we can use the functions in a module, we have to import it with an <span>**import statement**</span>:

    >>> import math

This statement creates a <span>**module object**</span> named math. If you display the module object, you get some information about it:

    >>> math
    <module 'math' (built-in)>

The module object contains the functions and variables defined in the module. To access one of the functions, you have to specify the name of the module and the name of the function, separated by a dot (also known as a period). This format is called <span>**dot notation**</span>.

    >>> ratio = signal_power / noise_power
    >>> decibels = 10 * math.log10(ratio)

    >>> radians = 0.7
    >>> height = math.sin(radians)

The first example uses `math.log10` to compute a signal-to-noise ratio in decibels (assuming that `signal_power` and `noise_power` are defined). The math module also provides <span>`log`</span>, which computes logarithms base <span>e</span>.

The second example finds the sine of <span>radians</span>. The name of the variable is a hint that <span>sin</span> and the other trigonometric functions (<span>cos</span>, <span>tan</span>, etc.) take arguments in radians. To convert from degrees to radians, divide by 180 and multiply by $\pi$:

    >>> degrees = 45
    >>> radians = degrees / 180.0 * math.pi
    >>> math.sin(radians)
    0.707106781187

The expression <span>`math.pi`</span> gets the variable <span>pi</span> from the math module. Its value is a floating-point approximation of $\pi$, accurate to about 15 digits.

If you know trigonometry, you can check the previous result by comparing it to the square root of two divided by two:

    >>> math.sqrt(2) / 2.0
    0.707106781187

