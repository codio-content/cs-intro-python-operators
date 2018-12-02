-----------

The <span>collections</span> module also provides <span>defaultdict</span>, which is like a dictionary except that if you access a key that doesn’t exist, it can generate a new value on the fly.

When you create a defaultdict, you provide a function that’s used to create new values. A function used to create objects is sometimes called a <span>**factory**</span>. The built-in functions that create lists, sets, and other types can be used as factories:

    >>> from collections import defaultdict
    >>> d = defaultdict(list)

Notice that the argument is <span>list</span>, which is a class object, not <span>list()</span>, which is a new list. The function you provide doesn’t get called unless you access a key that doesn’t exist.

    >>> t = d['new key']
    >>> t
    []

The new list, which we’re calling <span>t</span>, is also added to the dictionary. So if we modify <span>t</span>, the change appears in <span>d</span>:

    >>> t.append('new value')
    >>> d
    defaultdict(<class 'list'>, {'new key': ['new value']})

If you are making a dictionary of lists, you can often write simpler code using <span>defaultdict</span>. In my solution to Exercise [anagrams], which you can get from <http://thinkpython2.com/code/anagram_sets.py>, I make a dictionary that maps from a sorted string of letters to the list of words that can be spelled with those letters. For example, <span>’opst’</span> maps to the list .

Here’s the original code:

    def all_anagrams(filename):
        d = {}
        for line in open(filename):
            word = line.strip().lower()
            t = signature(word)
            if t not in d:
                d[t] = [word]
            else:
                d[t].append(word)
        return d

This can be simplified using <span>setdefault</span>, which you might have used in Exercise [setdefault]:

    def all_anagrams(filename):
        d = {}
        for line in open(filename):
            word = line.strip().lower()
            t = signature(word)
            d.setdefault(t, []).append(word)
        return d

This solution has the drawback that it makes a new list every time, regardless of whether it is needed. For lists, that’s no big deal, but if the factory function is complicated, it might be.

We can avoid this problem and simplify the code using a <span>defaultdict</span>:

    def all_anagrams(filename):
        d = defaultdict(list)
        for line in open(filename):
            word = line.strip().lower()
            t = signature(word)
            d[t].append(word)
        return d

My solution to Exercise [poker], which you can download from <http://thinkpython2.com/code/PokerHandSoln.py>, uses <span>setdefault</span> in the function `has_straightflush`. This solution has the drawback of creating a <span>Hand</span> object every time through the loop, whether it is needed or not. As an exercise, rewrite it using a defaultdict.

