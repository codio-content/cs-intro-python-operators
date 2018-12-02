--------------

The programs we have written so far accept no input from the user. They just do the same thing every time.

Python provides a built-in function called <span>input</span> that stops the program and waits for the user to type something. When the user presses <span>Return</span> or <span>Enter</span>, the program resumes and `input` returns what the user typed as a string. In Python 2, the same function is called `raw_input`.

    >>> text = input()
    What are you waiting for?
    >>> text
    'What are you waiting for?'

Before getting input from the user, it is a good idea to print a prompt telling the user what to type. `input` can take a prompt as an argument:

    >>> name = input('What...is your name?\n')
    What...is your name?
    Arthur, King of the Britons!
    >>> name
    'Arthur, King of the Britons!'

The sequence `\n` at the end of the prompt represents a <span>**newline**</span>, which is a special character that causes a line break. That’s why the user’s input appears below the prompt.

If you expect the user to type an integer, you can try to convert the return value to <span>int</span>:

    >>> prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
    >>> speed = input(prompt)
    What...is the airspeed velocity of an unladen swallow?
    42
    >>> int(speed)
    42

But if the user types something other than a string of digits, you get an error:

    >>> speed = input(prompt)
    What...is the airspeed velocity of an unladen swallow?
    What do you mean, an African or a European swallow?
    >>> int(speed)
    ValueError: invalid literal for int() with base 10

We will see how to handle this kind of error later.

