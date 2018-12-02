---------------

Any file that contains Python code can be imported as a module. For example, suppose you have a file named <span>wc.py</span> with the following code:

    def linecount(filename):
        count = 0
        for line in open(filename):
            count += 1
        return count

    print(linecount('wc.py'))

If you run this program, it reads itself and prints the number of lines in the file, which is 7. You can also import it like this:

    >>> import wc
    7

Now you have a module object <span>wc</span>:

    >>> wc
    <module 'wc' from 'wc.py'>

The module object provides `linecount`:

    >>> wc.linecount('wc.py')
    7

So that’s how you write modules in Python.

The only problem with this example is that when you import the module it runs the test code at the bottom. Normally when you import a module, it defines new functions but it doesn’t run them.

Programs that will be imported as modules often use the following idiom:

    if __name__ == '__main__':
        print(linecount('wc.py'))

`__name__` is a built-in variable that is set when the program starts. If the program is running as a script, `__name__` has the value `'__main__'`; in that case, the test code runs. Otherwise, if the module is being imported, the test code is skipped.

As an exercise, type this example into a file named <span>wc.py</span> and run it as a script. Then run the Python interpreter and <span>import wc</span>. What is the value of `__name__` when the module is being imported?

Warning: If you import a module that has already been imported, Python does nothing. It does not re-read the file, even if it has changed.

If you want to reload a module, you can use the built-in function <span>reload</span>, but it can be tricky, so the safest thing to do is restart the interpreter and then import the module again.

