--------------

Given a dictionary <span>d</span> and a key <span>k</span>, it is easy to find the corresponding value <span>v = d[k]</span>. This operation is called a <span>**lookup**</span>.

But what if you have <span>v</span> and you want to find <span>k</span>? You have two problems: first, there might be more than one key that maps to the value <span>v</span>. Depending on the application, you might be able to pick one, or you might have to make a list that contains all of them. Second, there is no simple syntax to do a <span>**reverse lookup**</span>; you have to search.

Here is a function that takes a value and returns the first key that maps to that value:

    def reverse_lookup(d, v):
        for k in d:
            if d[k] == v:
                return k
        raise LookupError()

This function is yet another example of the search pattern, but it uses a feature we haven’t seen before, <span>`raise`</span>. The <span>**raise statement**</span> causes an exception; in this case it causes a <span>LookupError</span>, which is a built-in exception used to indicate that a lookup operation failed.

If we get to the end of the loop, that means <span>v</span> doesn’t appear in the dictionary as a value, so we raise an exception.

Here is an example of a successful reverse lookup:

    >>> h = histogram('parrot')
    >>> key = reverse_lookup(h, 2)
    >>> key
    'r'

And an unsuccessful one:

    >>> key = reverse_lookup(h, 3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 5, in reverse_lookup
    LookupError

The effect when you raise an exception is the same as when Python raises one: it prints a traceback and an error message.

The <span>raise</span> statement can take a detailed error message as an optional argument. For example:

    >>> raise LookupError('value does not appear in the dictionary')
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    LookupError: value does not appear in the dictionary

A reverse lookup is much slower than a forward lookup; if you have to do it often, or if the dictionary gets big, the performance of your program will suffer.

