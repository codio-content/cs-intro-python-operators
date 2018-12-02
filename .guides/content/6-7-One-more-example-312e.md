----------------

After <span>factorial</span>, the most common example of a recursively defined mathematical function is <span>fibonacci</span>, which has the following definition (see <http://en.wikipedia.org/wiki/Fibonacci_number>):

$$\begin{aligned}
&& \mathrm{fibonacci}(0) = 0 \\
&& \mathrm{fibonacci}(1) = 1 \\
&& \mathrm{fibonacci}(n) = \mathrm{fibonacci}(n-1) + \mathrm{fibonacci}(n-2)\end{aligned}$$

Translated into Python, it looks like this:

    def fibonacci(n):
        if n == 0:
            return 0
        elif  n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

If you try to follow the flow of execution here, even for fairly small values of $n$, your head explodes. But according to the leap of faith, if you assume that the two recursive calls work correctly, then it is clear that you get the right result by adding them together.

