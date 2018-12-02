----------

Sometimes it is obvious what the attributes of an object should be, but other times you have to make decisions. For example, imagine you are designing a class to represent rectangles. What attributes would you use to specify the location and size of a rectangle? You can ignore angle; to keep things simple, assume that the rectangle is either vertical or horizontal.

There are at least two possibilities:

-   You could specify one corner of the rectangle (or the center), the width, and the height.

-   You could specify two opposing corners.

At this point it is hard to say whether either is better than the other, so we’ll implement the first one, just as an example.

Here is the class definition:

    class Rectangle:
        """Represents a rectangle. 

        attributes: width, height, corner.
        """

The docstring lists the attributes: <span>width</span> and <span>height</span> are numbers; <span>corner</span> is a Point object that specifies the lower-left corner.

To represent a rectangle, you have to instantiate a Rectangle object and assign values to the attributes:

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

The expression <span>box.corner.x</span> means, “Go to the object <span>box</span> refers to and select the attribute named <span>corner</span>; then go to that object and select the attribute named <span>x</span>.”

![image](/.guides/img/rectangle.jpg)



The Figure above shows the state of this object. An object that is an attribute of another object is <span>**embedded**</span>.

