------------------------

Some of the functions we have seen require arguments. For example, when you call <span>math.sin</span> you pass a number as an argument. Some functions take more than one argument: <span>math.pow</span> takes two, the base and the exponent.

Inside the function, the arguments are assigned to variables called <span>**parameters**</span>. Here is a definition for a function that takes an argument:

    def print_twice(bruce):
        print(bruce)
        print(bruce)

This function assigns the argument to a parameter named <span>bruce</span>. When the function is called, it prints the value of the parameter (whatever it is) twice.

This function works with any value that can be printed.

    >>> print_twice('Spam')
    Spam
    Spam
    >>> print_twice(42)
    42
    42
    >>> print_twice(math.pi)
    3.14159265359
    3.14159265359

The same rules of composition that apply to built-in functions also apply to programmer-defined functions, so we can use any kind of expression as an argument for `print_twice`:

    >>> print_twice('Spam '*4)
    Spam Spam Spam Spam
    Spam Spam Spam Spam
    >>> print_twice(math.cos(math.pi))
    -1.0
    -1.0

The argument is evaluated before the function is called, so in the examples the expressions `'Spam '*4` and <span>math.cos(math.pi)</span> are only evaluated once.

You can also use a variable as an argument:

    >>> michael = 'Eric, the half a bee.'
    >>> print_twice(michael)
    Eric, the half a bee.
    Eric, the half a bee.

The name of the variable we pass as an argument (<span>michael</span>) has nothing to do with the name of the parameter (<span>bruce</span>). It doesn’t matter what the value was called back home (in the caller); here in `print_twice`, we call everybody <span>bruce</span>.