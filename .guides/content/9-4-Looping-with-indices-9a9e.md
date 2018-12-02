--------------------

I wrote the functions in the previous section with <span>for</span> loops because I only needed the characters in the strings; I didn’t have to do anything with the indices.

For `is_abecedarian` we have to compare adjacent letters, which is a little tricky with a <span>for</span> loop:

    def is_abecedarian(word):
        previous = word[0]
        for c in word:
            if c < previous:
                return False
            previous = c
        return True

An alternative is to use recursion:

    def is_abecedarian(word):
        if len(word) <= 1:
            return True
        if word[0] > word[1]:
            return False
        return is_abecedarian(word[1:])

Another option is to use a <span>while</span> loop:

    def is_abecedarian(word):
        i = 0
        while i < len(word)-1:
            if word[i+1] < word[i]:
                return False
            i = i+1
        return True

The loop starts at <span>i=0</span> and ends when <span>i=len(word)-1</span>. Each time through the loop, it compares the $i$th character (which you can think of as the current character) to the $i+1$th character (which you can think of as the next).

If the next character is less than (alphabetically before) the current one, then we have discovered a break in the abecedarian trend, and we return <span>False</span>.

If we get to the end of the loop without finding a fault, then the word passes the test. To convince yourself that the loop ends correctly, consider an example like `'flossy'`. The length of the word is 6, so the last time the loop runs is when <span>i</span> is 4, which is the index of the second-to-last character. On the last iteration, it compares the second-to-last character to the last, which is what we want.

{Try It}(python3 code/word_play.py)

Here is a version of `is_palindrome` (see Chapter 6 Exercises) that uses two indices; one starts at the beginning and goes up; the other starts at the end and goes down.

    def is_palindrome(word):
        i = 0
        j = len(word)-1

        while i<j:
            if word[i] != word[j]:
                return False
            i = i+1
            j = j-1

        return True

Or we could reduce to a previously solved problem and write:

    def is_palindrome(word):
        return is_reverse(word, word)

Using `is_reverse` from Section 8.11.

