--------------------------

Functions can return instances. For example, `find_center` takes a <span>Rectangle</span> as an argument and returns a <span>Point</span> that contains the coordinates of the center of the <span>Rectangle</span>:

    def find_center(rect):
        p = Point()
        p.x = rect.corner.x + rect.width/2
        p.y = rect.corner.y + rect.height/2
        return p

Here is an example that passes <span>box</span> as an argument and assigns the resulting Point to <span>center</span>:

    >>> center = find_center(box)
    >>> print_point(center)
    (50, 100)

