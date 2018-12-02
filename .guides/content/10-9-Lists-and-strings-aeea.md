-----------------

A string is a sequence of characters and a list is a sequence of values, but a list of characters is not the same as a string. To convert from a string to a list of characters, you can use <span>list</span>:

    >>> s = 'spam'
    >>> t = list(s)
    >>> t
    ['s', 'p', 'a', 'm']

Because <span>list</span> is the name of a built-in function, you should avoid using it as a variable name. I also avoid <span>l</span> because it looks too much like <span>1</span>. So that’s why I use <span>t</span>.

The <span>list</span> function breaks a string into individual letters. If you want to break a string into words, you can use the <span>`split`</span> method:

    >>> s = 'pining for the fjords'
    >>> t = s.split()
    >>> t
    ['pining', 'for', 'the', 'fjords']

An optional argument called a <span>**delimiter**</span> specifies which characters to use as word boundaries. The following example uses a hyphen as a delimiter:

    >>> s = 'spam-spam-spam'
    >>> delimiter = '-'
    >>> t = s.split(delimiter)
    >>> t
    ['spam', 'spam', 'spam']

<span>`join`</span> is the inverse of <span>split</span>. It takes a list of strings and concatenates the elements. <span>join</span> is a string method, so you have to invoke it on the delimiter and pass the list as a parameter:

    >>> t = ['pining', 'for', 'the', 'fjords']
    >>> delimiter = ' '
    >>> s = delimiter.join(t)
    >>> s
    'pining for the fjords'

In this case the delimiter is a space character, so <span>join</span> puts a space between words. To concatenate strings without spaces, you can use the empty string, `''`, as a delimiter.

