import turtle

t = turtle.Turtle()

def recursive_tree(branch_length, t):
    """Draw a tree recursively"""
    if branch_length > 5:
        t.forward(branch_length)
        t.right(angle)
        recursive_tree(branch_length - 15, angle, t)
        t.left(angle * 2)
        recursive_tree(branch_length - 15, angle, t)
        t.right(angle)
        t.backwards(branch_length)
        
recursive_tree(90, t)
turtle.mainloop()