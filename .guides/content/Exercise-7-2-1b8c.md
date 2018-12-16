---------

The built-in function <span>`eval`</span> takes a string and evaluates it using the Python interpreter. For example:

    >>> eval('1 + 2 * 3')
    7
    >>> import math
    >>> eval('math.sqrt(5)')
    2.2360679774997898
    >>> eval('type(math.pi)')
    <class 'float'>

Write a function called `eval_loop` that iteratively prompts the user, takes the resulting input and evaluates it using <span>eval</span>, and prints the result.

It should continue until the user enters `'done'`, and then return the value of the last expression it evaluated.

{Try It}(python3 code/eval_loop.py)

{Check It!|assessment}(code-output-compare-18622402)

