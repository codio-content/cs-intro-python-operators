-----------

As you should expect by now, you can call one function from within another. As an example, we’ll write a function that takes two points, the center of the circle and a point on the perimeter, and computes the area of the circle.

Assume that the center point is stored in the variables <span>xc</span> and <span>yc</span>, and the perimeter point is in <span>xp</span> and <span>yp</span>. The first step is to find the radius of the circle, which is the distance between the two points. We just wrote a function, <span>distance</span>, that does that:

    radius = distance(xc, yc, xp, yp)

The next step is to find the area of a circle with that radius; we just wrote that, too:

    result = area(radius)

Encapsulating these steps in a function, we get:

    def circle_area(xc, yc, xp, yp):
        radius = distance(xc, yc, xp, yp)
        result = area(radius)
        return result

The temporary variables <span>radius</span> and <span>result</span> are useful for development and debugging, but once the program is working, we can make it more concise by composing the function calls:

    def circle_area(xc, yc, xp, yp):
        return area(distance(xc, yc, xp, yp))

