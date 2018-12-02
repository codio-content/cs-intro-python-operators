###
If something goes wrong during runtime, Python prints a message that includes the name of the exception, the line of the program where the problem occurred, and a traceback.

The traceback identifies the function that is currently running, and then the function that called it, and then the function that called <span>*that*</span>, and so on. In other words, it traces the sequence of function calls that got you to where you are, including the line number in your file where each call occurred.

The first step is to examine the place in the program where the error occurred and see if you can figure out what happened. These are some of the most common runtime errors:

NameError:
:   You are trying to use a variable that doesn’t exist in the current environment. Check if the name is spelled right, or at least consistently. And remember that local variables are local; you cannot refer to them from outside the function where they are defined.

TypeError:
:   There are several possible causes:

    -   You are trying to use a value improperly. Example: indexing a string, list, or tuple with something other than an integer.

    -   There is a mismatch between the items in a format string and the items passed for conversion. This can happen if either the number of items does not match or an invalid conversion is called for.

    -   You are passing the wrong number of arguments to a function. For methods, look at the method definition and check that the first parameter is <span>self</span>. Then look at the method invocation; make sure you are invoking the method on an object with the right type and providing the other arguments correctly.

KeyError:
:   You are trying to access an element of a dictionary using a key that the dictionary does not contain. If the keys are strings, remember that capitalization matters.

AttributeError:
:   You are trying to access an attribute or method that does not exist. Check the spelling! You can use the built-in function <span>vars</span> to list the attributes that do exist.

    If an AttributeError indicates that an object has <span>NoneType</span>, that means that it is <span>None</span>. So the problem is not the attribute name, but the object.

    The reason the object is none might be that you forgot to return a value from a function; if you get to the end of a function without hitting a <span>return</span> statement, it returns <span>None</span>. Another common cause is using the result from a list method, like <span>sort</span>, that returns <span>None</span>.

IndexError:
:   The index you are using to access a list, string, or tuple is greater than its length minus one. Immediately before the site of the error, add a <span>print</span> statement to display the value of the index and the length of the array. Is the array the right size? Is the index the right value?

The Python debugger (<span>pdb</span>) is useful for tracking down exceptions because it allows you to examine the state of the program immediately before the error. You can read about <span>pdb</span> at <https://docs.python.org/3/library/pdb.html>.

