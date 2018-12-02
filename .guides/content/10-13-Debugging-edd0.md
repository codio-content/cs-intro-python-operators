---------

Careless use of lists (and other mutable objects) can lead to long hours of debugging. Here are some common pitfalls and ways to avoid them:

1.  Most list methods modify the argument and return <span>None</span>. This is the opposite of the string methods, which return a new string and leave the original alone.

    If you are used to writing string code like this:

        word = word.strip()

    It is tempting to write list code like this:

        t = t.sort()           # WRONG!

    Because <span>sort</span> returns <span>None</span>, the next operation you perform with <span>t</span> is likely to fail.

    Before using list methods and operators, you should read the documentation carefully and then test them in interactive mode.

2.  Pick an idiom and stick with it.

    Part of the problem with lists is that there are too many ways to do things. For example, to remove an element from a list, you can use <span>pop</span>, <span>remove</span>, <span>del</span>, or even a slice assignment.

    To add an element, you can use the <span>append</span> method or the <span>+</span> operator. Assuming that <span>t</span> is a list and <span>x</span> is a list element, these are correct:

        t.append(x)
        t = t + [x]
        t += [x]

    And these are wrong:

        t.append([x])          # WRONG!
        t = t.append(x)        # WRONG!
        t + [x]                # WRONG!
        t = t + x              # WRONG!

    Try out each of these examples in interactive mode to make sure you understand what they do. Notice that only the last one causes a runtime error; the other three are legal, but they do the wrong thing.

3.  Make copies to avoid aliasing.

    If you want to use a method like <span>sort</span> that modifies the argument, but you need to keep the original list as well, you can make a copy.

        >>> t = [3, 1, 2]
        >>> t2 = t[:]
        >>> t2.sort()
        >>> t
        [3, 1, 2]
        >>> t2
        [1, 2, 3]

    In this example you could also use the built-in function <span>sorted</span>, which returns a new, sorted list and leaves the original alone.

        >>> t2 = sorted(t)
        >>> t
        [3, 1, 2]
        >>> t2
        [1, 2, 3]

