---------------
More anagrams!

1.  Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of words that are anagrams.

    Here is an example of what the output might look like:

        ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
        ['retainers', 'ternaries']
        ['generating', 'greatening']
        ['resmelts', 'smelters', 'termless']

    Hint: you might want to build a dictionary that maps from a collection of letters to a list of words that can be spelled with those letters. The question is, how can you represent the collection of letters in a way that can be used as a key?
    
{Try It}(python3 code/anagrams.py)

2.  Modify the previous program so that it prints the longest list of anagrams first, followed by the second longest, and so on.

{Try It}(python3 code/anagrams.py)

3.  In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on the board, to form an eight-letter word. What collection of 8 letters forms the most possible bingos? Hint: there are seven.

{Try It}(python3 code/anagrams.py)

Solution: <http://thinkpython2.com/code/anagram_sets.py>.