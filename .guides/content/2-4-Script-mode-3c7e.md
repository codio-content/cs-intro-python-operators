-----------

So far we have run Python in <span>**interactive mode**</span>, which means that you interact directly with the interpreter. Interactive mode is a good way to get started, but if you are working with more than a few lines of code, it can be clumsy.

The alternative is to save code in a file called a <span>**script**</span> and then run the interpreter in <span>**script mode**</span> to execute the script. By convention, Python scripts have names that end with <span>.py</span>.

If you know how to create and run a script on your computer, you are ready to go. Otherwise I recommend using PythonAnywhere again. I have posted instructions for running in script mode at <http://tinyurl.com/thinkpython2e>.

Because Python provides both modes, you can test bits of code in interactive mode before you put them in a script. But there are differences between interactive mode and script mode that can be confusing.

For example, if you are using Python as a calculator, you might type

    >>> miles = 26.2
    >>> miles * 1.61
    42.182
    
Give it a try here:
<iframe src="https://trinket.io/embed/console/c005e516ad" width="100%" height="200" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


<newline></newline>
The first line assigns a value to <span>miles</span>, but it has no visible effect. The second line is an expression, so the interpreter evaluates it and displays the result. It turns out that a marathon is about 42 kilometers.

But if you type the same code into a script and run it, you get no output at all. 

{Run Script}(python code/script_mode.py)

In script mode an expression, all by itself, has no visible effect. Python actually evaluates the expression, but it doesn’t display the value unless you tell it to:

    miles = 26.2
    print(miles * 1.61)

This behavior can be confusing at first.

A script usually contains a sequence of statements. If there is more than one statement, the results appear one at a time as the statements execute.

For example, the script

    print(1)
    x = 2
    print(x)

produces the output

    1
    2

The assignment statement produces no output.

{Run Script| terminal}(python code/script_mode.py)

To check your understanding, type the following statements in the Python interpreter and see what they do:

    5
    x = 5
    x + 1

<iframe src="https://trinket.io/embed/console/c005e516ad" width="100%" height="200" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

<newline></newline>
Now put the same statements in a script and run it. 

{Run Script}(python code/script_mode.py)

What is the output? Modify the script by transforming each expression into a print statement and then run it again.

