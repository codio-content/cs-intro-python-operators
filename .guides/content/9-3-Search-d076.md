------

All of the exercises in the previous section have something in common; they can be solved with the search pattern we saw in Section 8.6. The simplest example is:

    def has_no_e(word):
        for letter in word:
            if letter == 'e':
                return False
        return True

The <span>for</span> loop traverses the characters in <span>word</span>. If we find the letter “e”, we can immediately return <span>False</span>; otherwise we have to go to the next letter. If we exit the loop normally, that means we didn’t find an “e”, so we return <span>True</span>.

You could write this function more concisely using the <span>in</span> operator, but I started with this version because it demonstrates the logic of the search pattern.

{Try It}(python3 code/word_play.py)

`avoids` is a more general version of `has_no_e` but it has the same structure:

    def avoids(word, forbidden):
        for letter in word:
            if letter in forbidden:
                return False
        return True

We can return <span>False</span> as soon as we find a forbidden letter; if we get to the end of the loop, we return <span>True</span>.

`uses_only` is similar except that the sense of the condition is reversed:

    def uses_only(word, available):
        for letter in word: 
            if letter not in available:
                return False
        return True

Instead of a list of forbidden letters, we have a list of available letters. If we find a letter in <span>word</span> that is not in <span>available</span>, we can return <span>False</span>.

{Try It}(python3 code/word_play.py)

`uses_all` is similar except that we reverse the role of the word and the string of letters:

    def uses_all(word, required):
        for letter in required: 
            if letter not in word:
                return False
        return True

Instead of traversing the letters in <span>word</span>, the loop traverses the required letters. If any of the required letters do not appear in the word, we can return <span>False</span>.

If you were really thinking like a computer scientist, you would have recognized that `uses_all` was an instance of a previously solved problem, and you would have written:

    def uses_all(word, required):
        return uses_only(required, word)

This is an example of a program development plan called <span>**reduction to a previously solved problem**</span>, which means that you recognize the problem you are working on as an instance of a solved problem and apply an existing solution.

