----------------

A <span>**value**</span> is one of the basic things a program works with, like a letter or a number. Some values we have seen so far are <span STYLE="font-family: courier">2</span>, <span STYLE="font-family: courier">42.0</span>, and `'Hello, World!'`.

These values belong to different <span>**types**</span>: <span STYLE="font-family: courier">2</span> is an <span>**integer**</span>, <span STYLE="font-family: courier">42.0</span> is a <span>**floating-point number**</span>, and `'Hello, World!'` is a <span>**string**</span>, so-called because the letters it contains are strung together.

If you are not sure what type a value has, the interpreter can tell you:

    >>> type(2)
    <class 'int'>
    >>> type(42.0)
    <class 'float'>
    >>> type('Hello, World!')
    <class 'str'>

In these results, the word “class” is used in the sense of a category; a type is a category of values.

Not surprisingly, integers belong to the type <span STYLE="font-family: courier">int</span>, strings belong to <span STYLE="font-family: courier">str</span> and floating-point numbers belong to <span STYLE="font-family: courier">float</span>.

What about values like <span STYLE="font-family: courier">'2'</span> and <span STYLE="font-family: courier">'42.0'</span>? They look like numbers, but they are in quotation marks like strings.

    >>> type('2')
    <class 'str'>
    >>> type('42.0')
    <class 'str'>

They’re strings.

When you type a large integer, you might be tempted to use commas between groups of digits, as in <span>1,000,000</span>. This is not a legal <span>*integer*</span> in Python, but it is legal:

    >>> 1,000,000
    (1, 0, 0)

That’s not what we expected at all! Python interprets <span>1,000,000</span> as a comma-separated sequence of integers. We’ll learn more about this kind of sequence later.

