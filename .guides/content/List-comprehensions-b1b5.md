-------------------

In Section [filter] we saw the map and filter patterns. For example, this function takes a list of strings, maps the string method <span>capitalize</span> to the elements, and returns a new list of strings:

    def capitalize_all(t):
        res = []
        for s in t:
            res.append(s.capitalize())
        return res

We can write this more concisely using a <span>**list comprehension**</span>:

    def capitalize_all(t):
        return [s.capitalize() for s in t]

The bracket operators indicate that we are constructing a new list. The expression inside the brackets specifies the elements of the list, and the <span>for</span> clause indicates what sequence we are traversing.

The syntax of a list comprehension is a little awkward because the loop variable, <span>s</span> in this example, appears in the expression before we get to the definition.

List comprehensions can also be used for filtering. For example, this function selects only the elements of <span>t</span> that are upper case, and returns a new list:

    def only_upper(t):
        res = []
        for s in t:
            if s.isupper():
                res.append(s)
        return res

We can rewrite it using a list comprehension

    def only_upper(t):
        return [s for s in t if s.isupper()]

List comprehensions are concise and easy to read, at least for simple expressions. And they are usually faster than the equivalent for loops, sometimes much faster. So if you are mad at me for not mentioning them earlier, I understand.

But, in my defense, list comprehensions are harder to debug because you can’t put a print statement inside the loop. I suggest that you use them only if the computation is simple enough that you are likely to get it right the first time. And for beginners that means never.

