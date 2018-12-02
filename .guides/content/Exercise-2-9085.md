If you download my solution to Exercise [anagrams] from <http://thinkpython2.com/code/anagram_sets.py>, you’ll see that it creates a dictionary that maps from a sorted string of letters to the list of words that can be spelled with those letters. For example, `'opst'` maps to the list `['opts', 'post', 'pots', 'spot', 'stop', 'tops']`.

Write a module that imports `anagram_sets` and provides two new functions: `store_anagrams` should store the anagram dictionary in a “shelf”; `read_anagrams` should look up a word and return a list of its anagrams. 

{Try It}(python3 code/anagrams_sets_0.py)


Solution: <http://thinkpython2.com/code/anagram_db.py>.