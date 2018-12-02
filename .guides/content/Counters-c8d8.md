--------

A Counter is like a set, except that if an element appears more than once, the Counter keeps track of how many times it appears. If you are familiar with the mathematical idea of a <span>**multiset**</span>, a Counter is a natural way to represent a multiset.

Counter is defined in a standard module called <span>collections</span>, so you have to import it. You can initialize a Counter with a string, list, or anything else that supports iteration:

    >>> from collections import Counter
    >>> count = Counter('parrot')
    >>> count
    Counter({'r': 2, 't': 1, 'o': 1, 'p': 1, 'a': 1})

Counters behave like dictionaries in many ways; they map from each key to the number of times it appears. As in dictionaries, the keys have to be hashable.

Unlike dictionaries, Counters don’t raise an exception if you access an element that doesn’t appear. Instead, they return 0:

    >>> count['d']
    0

We can use Counters to rewrite `is_anagram` from Exercise [anagram]:

    def is_anagram(word1, word2):
        return Counter(word1) == Counter(word2)

If two words are anagrams, they contain the same letters with the same counts, so their Counters are equivalent.

Counters provide methods and operators to perform set-like operations, including addition, subtraction, union and intersection. And they provide an often-useful method, `most_common`, which returns a list of value-frequency pairs, sorted from most common to least:

    >>> count = Counter('parrot')
    >>> for val, freq in count.most_common(3):
    ...     print(val, freq)
    r 2
    p 1
    a 1

