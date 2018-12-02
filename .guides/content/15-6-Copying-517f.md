-------

Aliasing can make a program difficult to read because changes in one place might have unexpected effects in another place. It is hard to keep track of all the variables that might refer to a given object.

Copying an object is often an alternative to aliasing. The <span>copy</span> module contains a function called <span>copy</span> that can duplicate any object:

    >>> p1 = Point()
    >>> p1.x = 3.0
    >>> p1.y = 4.0

    >>> import copy
    >>> p2 = copy.copy(p1)

<span>`p1`</span> and <span>`p2`</span> contain the same data, but they are not the same Point.

    >>> print_point(p1)
    (3, 4)
    >>> print_point(p2)
    (3, 4)
    >>> p1 is p2
    False
    >>> p1 == p2
    False

The <span>`is`</span> operator indicates that <span>p1</span> and <span>p2</span> are not the same object, which is what we expected. But you might have expected <span> == </span> to yield <span>True</span> because these points contain the same data. In that case, you will be disappointed to learn that for instances, the default behavior of the <span>==</span> operator is the same as the <span>is</span> operator; it checks object identity, not object equivalence. That’s because for programmer-defined types, Python doesn’t know what should be considered equivalent. At least, not yet.

If you use <span>copy.copy</span> to duplicate a Rectangle, you will find that it copies the Rectangle object but not the embedded Point.

    >>> box2 = copy.copy(box)
    >>> box2 is box
    False
    >>> box2.corner is box.corner
    True

![image](/.guides/img/rectangle2.jpg)



The Figure above shows what the object diagram looks like. This operation is called a <span>**shallow copy**</span> because it copies the object and any references it contains, but not the embedded objects.

For most applications, this is not what you want. In this example, invoking `grow_rectangle` on one of the Rectangles would not affect the other, but invoking `move_rectangle` on either would affect both! This behavior is confusing and error-prone.

Fortunately, the <span>copy</span> module provides a method named <span>deepcopy</span> that copies not only the object but also the objects it refers to, and the objects <span>*they*</span> refer to, and so on. You will not be surprised to learn that this operation is called a <span>**deep copy**</span>.

    >>> box3 = copy.deepcopy(box)
    >>> box3 is box
    False
    >>> box3.corner is box.corner
    False

<span>box3</span> and <span>box</span> are completely separate objects.

As an exercise, write a version of `move_rectangle` that creates and returns a new Rectangle instead of modifying the old one.

