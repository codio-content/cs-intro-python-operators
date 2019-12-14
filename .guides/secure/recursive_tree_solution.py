import turtle

t = turtle.Turtle()

def recursive_tree(branch_length, angle, t):
    """Draw a tree recursively"""
    if branch_length > 5:
        t.forward(branch_length)
        t.right(angle)
        recursive_tree(branch_length - 15, angle, t)
        t.left(angle * 2)
        recursive_tree(branch_length - 15, angle, t)
        t.right(angle)
        t.backward(branch_length)
        
recursive_tree(45, 20, t)

turtle.mainloop()