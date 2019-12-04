----------

## Function Composition

Function composition is similar to helper functions in that two or more functions are used together to complete a larger task. However, function composition is a specific way in which functions are combined. Instead of calling the helper function from within another function, the helper function is called as a parameter of the function it is helping.

![Function Composition](.guides/images/function-composition.png)

It is important to note that the function definition for `area` **does not** take a function as a parameter. It expects a value (the radius of the circle). There is an order of operation for function composition. The `radius` function is executed first, and then the value it returns is passed to the `area` function.

```python
import math

def area(r):
    """Area of a circle"""
    return(math.pi * r ** 2)

def radius(x1, y1, x2, y2):
    """Distance formula to calculate the radius"""
    return(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

print(area(radius(0, 0, 4, 4)))
```

{try it}(python3 code/functions/function-composition.py 1)

|||challenge
## Function Composition for Pi
Create a function that calculates an approximation of pi. Use function composition to incorporate the value of pi with the `area` function. The approximation of pi can be done in a variety of ways:
* $$\pi$$ = circumference / diameter.
* $$\pi$$ = `x` * sine (180 / `x`). **Note**, the bigger the number used for `x`, the more accurate the approximation will be.
* $$\pi$$ = the number of radians in 180 degrees.
<details><summary>**Solution**</summary>Here is one possible solution.<img src=".guides/images/pi-function-composition.png" /></details>

|||

{try it}(python3 code/functions/function-composition.py 2)

## Function Composition vs Helper Functions

Both function composition and helper functions provide the same functionality. Using one over the other will not affect the end result. However, function composition offers improved readability. Look at the two function calls below:

```python
circle_area1(x1, y1, x2, y2)
circle_area2(radius(x1, y1, x2, y2, pi()))
```

Without seeing the function definitions, it is not clear how area can be derived from two points on a Cartesian plane in the first function call. The second function makes it very clear that the radius and pi are being used to calculate the area.

Another difference between the two is that helper functions can only be used with user-defined functions. You do not have access to the function definitions for the built-in functions for Python, so you cannot call a helper function from within a built-in function. You can, however, use function composition to combine built-in functions to accomplish a larger task.

```python
import math

print(math.sqrt(int("25")))
```

{try it}(python3 code/functions/function-composition.py 3)

|||challenge
## What happens if you:
* Add the print statement `print(math.pow(int("2"), int("3")))`?

|||

{try it}(python3 code/functions/function-composition.py 4)

<details><summary>**Limits of Function Composition and Readability**</summary>Function composition can improve readability, but there is a limit. The following code is an example of function composition taken too far.<br> <code>print(len(str(math.sqrt(math.pow(3, math.degrees(math.sin(5.79)))))))</code><br>This may be valid code and Python may not have any trouble understanding the code, it is not very readable for humans. Instead, try breaking the function composition into smaller, more accessible parts.<img src=".guides/images/multistep-function-composition.png" /></details>

{Check It!|assessment}(multiple-choice-2948315125)
