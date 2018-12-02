--------------------------------------

Suppose you are given a string and you want to count how many times each letter appears. There are several ways you could do it:

1.  You could create 26 variables, one for each letter of the alphabet. Then you could traverse the string and, for each character, increment the corresponding counter, probably using a chained conditional.

2.  You could create a list with 26 elements. Then you could convert each character to a number (using the built-in function <span>ord</span>), use the number as an index into the list, and increment the appropriate counter.

3.  You could create a dictionary with characters as keys and counters as the corresponding values. The first time you see a character, you would add an item to the dictionary. After that you would increment the value of an existing item.

Each of these options performs the same computation, but each of them implements that computation in a different way.

An <span>**implementation**</span> is a way of performing a computation; some implementations are better than others. For example, an advantage of the dictionary implementation is that we don’t have to know ahead of time which letters appear in the string and we only have to make room for the letters that do appear.

Here is what the code might look like:

    def histogram(s):
        d = dict()
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        return d

The name of the function is <span>histogram</span>, which is a statistical term for a collection of counters (or frequencies).

The first line of the function creates an empty dictionary. The <span>for</span> loop traverses the string. Each time through the loop, if the character <span>c</span> is not in the dictionary, we create a new item with key <span>c</span> and the initial value 1 (since we have seen this letter once). If <span>c</span> is already in the dictionary we increment <span>d[c]</span>.

Here’s how it works:

    >>> h = histogram('brontosaurus')
    >>> h
    {'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}

The histogram indicates that the letters `'a'` and `'b'` appear once; `'o'` appears twice, and so on.

Dictionaries have a method called <span>get</span> that takes a key and a default value. If the key appears in the dictionary, <span>get</span> returns the corresponding value; otherwise it returns the default value. For example:

    >>> h = histogram('a')
    >>> h
    {'a': 1}
    >>> h.get('a', 0)
    1
    >>> h.get('b', 0)
    0

As an exercise, use <span>get</span> to write <span>histogram</span> more concisely. You should be able to eliminate the <span>if</span> statement.

