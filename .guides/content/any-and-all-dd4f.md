-------------------------------------

Python provides a built-in function, <span>any</span>, that takes a sequence of boolean values and returns <span>True</span> if any of the values are <span>True</span>. It works on lists:

    >>> any([False, False, True])
    True

But it is often used with generator expressions:

    >>> any(letter == 't' for letter in 'monty')
    True

That example isn’t very useful because it does the same thing as the <span>in</span> operator. But we could use <span>any</span> to rewrite some of the search functions we wrote in Section [search]. For example, we could write <span>avoids</span> like this:

    def avoids(word, forbidden):
        return not any(letter in forbidden for letter in word)

The function almost reads like English, “<span>word</span> avoids <span>forbidden</span> if there are not any forbidden letters in <span>word</span>.”

Using <span>any</span> with a generator expression is efficient because it stops immediately if it finds a <span>True</span> value, so it doesn’t have to evaluate the whole sequence.

Python provides another built-in function, <span>all</span>, that returns <span>True</span> if every element of the sequence is <span>True</span>. As an exercise, use <span>all</span> to re-write `uses_all` from Section [search].

