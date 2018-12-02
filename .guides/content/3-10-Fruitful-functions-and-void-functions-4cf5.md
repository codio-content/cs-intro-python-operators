-------------------------------------

Some of the functions we have used, such as the math functions, return results; for lack of a better name, I call them <span>**fruitful functions**</span>. Other functions, like `print_twice`, perform an action but don’t return a value. They are called <span>**void functions**</span>.

When you call a fruitful function, you almost always want to do something with the result; for example, you might assign it to a variable or use it as part of an expression:

    x = math.cos(radians)
    golden = (math.sqrt(5) + 1) / 2

When you call a function in interactive mode, Python displays the result:

    >>> math.sqrt(5)
    2.2360679774997898

But in a script, if you call a fruitful function all by itself, the return value is lost forever!

    math.sqrt(5)

This script computes the square root of 5, but since it doesn’t store or display the result, it is not very useful.

Void functions might display something on the screen or have some other effect, but they don’t have a return value. If you assign the result to a variable, you get a special value called <span>None</span>.

    >>> result = print_twice('Bing')
    Bing
    Bing
    >>> print(result)
    None

The value <span>None</span> is not the same as the string `'None'`. It is a special value that has its own type:

    >>> type(None)
    <class 'NoneType'>

The functions we have written so far are all void. We will start writing fruitful functions in a few chapters.

