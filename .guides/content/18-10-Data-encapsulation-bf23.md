------------------

The previous chapters demonstrate a development plan we might call “object-oriented design”. We identified objects we needed—like <span>Point</span>, <span>Rectangle</span> and <span>Time</span>—and defined classes to represent them. In each case there is an obvious correspondence between the object and some entity in the real world (or at least a mathematical world).

But sometimes it is less obvious what objects you need and how they should interact. In that case you need a different development plan. In the same way that we discovered function interfaces by encapsulation and generalization, we can discover class interfaces by <span>**data encapsulation**</span>.

Markov analysis, from Section 13.8, provides a good example. If you download my code from <http://thinkpython2.com/code/markov.py>, you’ll see that it uses two global variables—`suffix_map` and `prefix`—that are read and written from several functions.

    suffix_map = {}        
    prefix = ()            

Because these variables are global, we can only run one analysis at a time. If we read two texts, their prefixes and suffixes would be added to the same data structures (which makes for some interesting generated text).

To run multiple analyses, and keep them separate, we can encapsulate the state of each analysis in an object. Here’s what that looks like:

    class Markov:

        def __init__(self):
            self.suffix_map = {}
            self.prefix = ()    

Next, we transform the functions into methods. For example, here’s `process_word`:

        def process_word(self, word, order=2):
            if len(self.prefix) < order:
                self.prefix += (word,)
                return

            try:
                self.suffix_map[self.prefix].append(word)
            except KeyError:
                # if there is no entry for this prefix, make one
                self.suffix_map[self.prefix] = [word]

            self.prefix = shift(self.prefix, word)        

Transforming a program like this—changing the design without changing the behavior—is another example of refactoring (see Section 4.7).

This example suggests a development plan for designing objects and methods:

1.  Start by writing functions that read and write global variables (when necessary).

2.  Once you get the program working, look for associations between global variables and the functions that use them.

3.  Encapsulate related variables as attributes of an object.

4.  Transform the associated functions into methods of the new class.

As an exercise, download my Markov code from <http://thinkpython2.com/code/markov.py>, and follow the steps described above to encapsulate the global variables as attributes of a new class called <span>Markov</span>. Solution: <http://thinkpython2.com/code/Markov.py> (note the capital M).

