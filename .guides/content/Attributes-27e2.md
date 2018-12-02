----------

You can assign values to an instance using dot notation:

    >>> blank.x = 3.0
    >>> blank.y = 4.0

This syntax is similar to the syntax for selecting a variable from a module, such as <span>math.pi</span> or <span>string.whitespace</span>. In this case, though, we are assigning values to named elements of an object. These elements are called <span>**attributes**</span>.

As a noun, “AT-trib-ute” is pronounced with emphasis on the first syllable, as opposed to “a-TRIB-ute”, which is a verb.

The following diagram shows the result of these assignments. A state diagram that shows an object and its attributes is called an <span>**object diagram**</span>; see Figure .

![image](/.guides/img/point.jpg)



The variable <span>blank</span> refers to a Point object, which contains two attributes. Each attribute refers to a floating-point number.

You can read the value of an attribute using the same syntax:

    >>> blank.y
    4.0
    >>> x = blank.x
    >>> x
    3.0

The expression <span>blank.x</span> means, “Go to the object <span>blank</span> refers to and get the value of <span>x</span>.” In the example, we assign that value to a variable named <span>x</span>. There is no conflict between the variable <span>x</span> and the attribute <span>x</span>.

You can use dot notation as part of any expression. For example:

    >>> '(%g, %g)' % (blank.x, blank.y)
    '(3.0, 4.0)'
    >>> distance = math.sqrt(blank.x**2 + blank.y**2)
    >>> distance
    5.0

You can pass an instance as an argument in the usual way. For example:

    def print_point(p):
        print('(%g, %g)' % (p.x, p.y))

`print_point` takes a point as an argument and displays it in mathematical notation. To invoke it, you can pass <span>blank</span> as an argument:

    >>> print_point(blank)
    (3.0, 4.0)

Inside the function, <span>p</span> is an alias for <span>blank</span>, so if the function modifies <span>p</span>, <span>blank</span> changes.

As an exercise, write a function called `distance_between_points` that takes two Points as arguments and returns the distance between them.

