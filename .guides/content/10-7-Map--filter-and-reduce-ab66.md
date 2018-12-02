----------------------

To add up all the numbers in a list, you can use a loop like this:

    def add_all(t):
        total = 0
        for x in t:
            total += x
        return total

<span>`total`</span> is initialized to 0. Each time through the loop, <span>x</span> gets one element from the list. The <span>+=</span> operator provides a short way to update a variable. This <span>**augmented assignment statement**</span>,

        total += x

is equivalent to

        total = total + x

As the loop runs, <span>total</span> accumulates the sum of the elements; a variable used this way is sometimes called an <span>**accumulator**</span>.

Adding up the elements of a list is such a common operation that Python provides it as a built-in function, <span>sum</span>:

    >>> t = [1, 2, 3]
    >>> sum(t)
    6

An operation like this that combines a sequence of elements into a single value is sometimes called <span>**reduce**</span>.

Sometimes you want to traverse one list while building another. For example, the following function takes a list of strings and returns a new list that contains capitalized strings:

    def capitalize_all(t):
        res = []
        for s in t:
            res.append(s.capitalize())
        return res

<span>`res`</span> is initialized with an empty list; each time through the loop, we append the next element. So <span>res</span> is another kind of accumulator.

An operation like `capitalize_all` is sometimes called a <span>**map**</span> because it “maps” a function (in this case the method <span>capitalize</span>) onto each of the elements in a sequence.

Another common operation is to select some of the elements from a list and return a sublist. For example, the following function takes a list of strings and returns a list that contains only the uppercase strings:

    def only_upper(t):
        res = []
        for s in t:
            if s.isupper():
                res.append(s)
        return res

<span>`isupper`</span> is a string method that returns <span>True</span> if the string contains only upper case letters.

An operation like `only_upper` is called a <span>**filter**</span> because it selects some of the elements and filters out the others.

Most common list operations can be expressed as a combination of map, filter and reduce.

