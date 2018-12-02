--------------

Strings provide methods that perform a variety of useful operations. A method is similar to a function—it takes arguments and returns a value—but the syntax is different. For example, the method <span>upper</span> takes a string and returns a new string with all uppercase letters.

Instead of the function syntax <span>upper(word)</span>, it uses the method syntax <span>word.upper()</span>.

    >>> word = 'banana'
    >>> new_word = word.upper()
    >>> new_word
    'BANANA'

This form of dot notation specifies the name of the method, <span>upper</span>, and the name of the string to apply the method to, <span>word</span>. The empty parentheses indicate that this method takes no arguments.

A method call is called an <span>**invocation**</span>; in this case, we would say that we are invoking <span>upper</span> on <span>word</span>.

As it turns out, there is a string method named <span>find</span> that is remarkably similar to the function we wrote:

    >>> word = 'banana'
    >>> index = word.find('a')
    >>> index
    1

In this example, we invoke <span>find</span> on <span>word</span> and pass the letter we are looking for as a parameter.

Actually, the <span>find</span> method is more general than our function; it can find substrings, not just characters:

    >>> word.find('na')
    2

By default, <span>find</span> starts at the beginning of the string, but it can take a second argument, the index where it should start:

    >>> word.find('na', 3)
    4

This is an example of an <span>**optional argument**</span>; <span>find</span> can also take a third argument, the index where it should stop:

    >>> name = 'bob'
    >>> name.find('b', 1, 2)
    -1

This search fails because <span>b</span> does not appear in the index range from <span>1</span> to <span>2</span>, not including <span>2</span>. Searching up to, but not including, the second index makes <span>find</span> consistent with the slice operator.

