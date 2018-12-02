--------------------

So far, we have only been using the functions that come with Python, but it is also possible to add new functions. A <span>**function definition**</span> specifies the name of a new function and the sequence of statements that run when the function is called.

Here is an example:

    def print_lyrics():
        print("I'm a lumberjack, and I'm okay.")
        print("I sleep all night and I work all day.")

<span>def</span> is a keyword that indicates that this is a function definition. The name of the function is `print_lyrics`. The rules for function names are the same as for variable names: letters, numbers and underscore are legal, but the first character can’t be a number. You can’t use a keyword as the name of a function, and you should avoid having a variable and a function with the same name.

The empty parentheses after the name indicate that this function doesn’t take any arguments.

The first line of the function definition is called the <span>**header**</span>; the rest is called the <span>**body**</span>. The header has to end with a colon and the body has to be indented. By convention, indentation is always four spaces. The body can contain any number of statements.

The strings in the print statements are enclosed in double quotes. Single quotes and double quotes do the same thing; most people use single quotes except in cases like this where a single quote (which is also an apostrophe) appears in the string.

All quotation marks (single and double) must be “straight quotes”, usually located next to Enter on the keyboard. “Curly quotes”, like the ones in this sentence, are not legal in Python.

If you type a function definition in interactive mode, the interpreter prints dots (<span>...</span>) to let you know that the definition isn’t complete:

    >>> def print_lyrics():
    ...     print("I'm a lumberjack, and I'm okay.")
    ...     print("I sleep all night and I work all day.")
    ...

To end the function, you have to enter an empty line.

Defining a function creates a <span>**function object**</span>, which has type `function`:

    >>> print(print_lyrics)
    <function print_lyrics at 0xb7e99e9c>
    >>> type(print_lyrics)
    <class 'function'>

The syntax for calling the new function is the same as for built-in functions:

    >>> print_lyrics()
    I'm a lumberjack, and I'm okay.
    I sleep all night and I work all day.

Once you have defined a function, you can use it inside another function. For example, to repeat the previous refrain, we could write a function called `repeat_lyrics`:

    def repeat_lyrics():
        print_lyrics()
        print_lyrics()

And then call `repeat_lyrics`:

    >>> repeat_lyrics()
    I'm a lumberjack, and I'm okay.
    I sleep all night and I work all day.
    I'm a lumberjack, and I'm okay.
    I sleep all night and I work all day.

But that’s not really how the song goes.

