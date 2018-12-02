-----------------

To find the most common words, we can make a list of tuples, where each tuple contains a word and its frequency, and sort it.

The following function takes a histogram and returns a list of word-frequency tuples:

    def most_common(hist):
        t = []
        for key, value in hist.items():
            t.append((value, key))

        t.sort(reverse=True)
        return t

In each tuple, the frequency appears first, so the resulting list is sorted by frequency. Here is a loop that prints the ten most common words:

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:10]:
        print(word, freq, sep='\t')

I use the keyword argument <span>`sep`</span> to tell <span>print</span> to use a tab character as a “separator”, rather than a space, so the second column is lined up. Here are the results from <span>*Emma*</span>:

    The most common words are:
    to      5242
    the     5205
    and     4897
    of      4295
    i       3191
    a       3130
    it      2529
    her     2483
    was     2400
    she     2364

This code can be simplified using the <span>`key`</span> parameter of the <span>sort</span> function. If you are curious, you can read about it at <https://wiki.python.org/moin/HowTo/Sorting>.

