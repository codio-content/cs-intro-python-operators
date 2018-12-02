---------

There are solutions to these exercises in the next section. You should at least attempt each one before you read the solutions.

1. Write a program that reads <span>words.txt</span> and prints only the words with more than 20 characters (not counting whitespace).  words.txt is located in the code directory, which is the same directory as the word_play.py file.

{Try It}(python3 code/word_play.py)

2. In 1939 Ernest Vincent Wright published a 50,000 word novel called <span>*Gadsby*</span> that does not contain the letter “e”. Since “e” is the most common letter in English, that’s not easy to do.

   In fact, it is difficult to construct a solitary thought without using that most common symbol. It is slow going at first, but with caution and hours of training you can gradually gain facility.

   All right, I’ll stop now.

   Write a function called `has_no_e` that returns <span>True</span> if the given word doesn’t have the letter “e” in it.

   Modify your program from the previous section to print only the words that have no “e” and compute the percentage of the words in the list that have no “e”.

3. Write a function named <span>avoids</span> that takes a word and a string of forbidden letters, and that returns <span>True</span> if the word doesn’t use any of the forbidden letters.

   Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes the smallest number of words?

{Try It}(python3 code/word_play.py)

4. Write a function named `uses_only` that takes a word and a string of letters, and that returns <span>True</span> if the word contains only letters in the list. Can you make a sentence using only the letters <span>acefhlo</span>? Other than “Hoe alfalfa?”

5. Write a function named `uses_all` that takes a word and a string of required letters, and that returns <span>True</span> if the word uses all the required letters at least once. How many words are there that use all the vowels <span>aeiou</span>? How about <span>aeiouy</span>?

6. Write a function called `is_abecedarian` that returns <span>True</span> if the letters in a word appear in alphabetical order (double letters are ok). How many abecedarian words are there?

{Try It}(python3 code/word_play.py)

