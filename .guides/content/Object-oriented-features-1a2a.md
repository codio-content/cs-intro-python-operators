------------------------

Python is an <span>**object-oriented programming language**</span>, which means that it provides features that support object-oriented programming, which has these defining characteristics:

-   Programs include class and method definitions.

-   Most of the computation is expressed in terms of operations on objects.

-   Objects often represent things in the real world, and methods often correspond to the ways things in the real world interact.

For example, the <span>Time</span> class defined in Chapter [time] corresponds to the way people record the time of day, and the functions we defined correspond to the kinds of things people do with times. Similarly, the <span>Point</span> and <span>Rectangle</span> classes in Chapter [clobjects] correspond to the mathematical concepts of a point and a rectangle.

So far, we have not taken advantage of the features Python provides to support object-oriented programming. These features are not strictly necessary; most of them provide alternative syntax for things we have already done. But in many cases, the alternative is more concise and more accurately conveys the structure of the program.

For example, in <span>Time1.py</span> there is no obvious connection between the class definition and the function definitions that follow. With some examination, it is apparent that every function takes at least one <span>Time</span> object as an argument.

This observation is the motivation for <span>**methods**</span>; a method is a function that is associated with a particular class. We have seen methods for strings, lists, dictionaries and tuples. In this chapter, we will define methods for programmer-defined types.

Methods are semantically the same as functions, but there are two syntactic differences:

-   Methods are defined inside a class definition in order to make the relationship between the class and the method explicit.

-   The syntax for invoking a method is different from the syntax for calling a function.

In the next few sections, we will take the functions from the previous two chapters and transform them into methods. This transformation is purely mechanical; you can do it by following a sequence of steps. If you are comfortable converting from one form to another, you will be able to choose the best form for whatever you are doing.

