"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import math
import turtle

# from TurtleWorld import *

# world = TurtleWorld()
# 
bob = Turtle()

def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)

square(bob)
wait_for_user()

def polygon(t, length, n):
    t = Turtle()
    for i in range(n):
        fd(t, length)
        lt(t, 360 / n)

polygon(bob, 50, 8)
wait_for_user()

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)




# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw a circle centered on the origin
    # radius = 100
    # bob.pu()
    # bob.fd(radius)
    # bob.lt(90)
    # bob.pd()
    # circle(bob, radius)

    # wait for the user to close the window
    turtle.mainloop()
