import turtle

t = turtle.Turtle()
t.speed(10)

def sierpinski(length, n):
    if n == 1:
        draw_triangle(length)
    else:
      sierpinski(length, n-1)
      t.rt(120)
      t.fd(length * 2**(n-2))
      sierpinski(length, n-1)
      t.lt(120)               
      t.fd(length * 2**(n-2)) 
      sierpinski(length, n-1)
      t.fd(length * 2**(n-2))  
         
def draw_triangle(length):
    t.setheading(180)      
    for i in range(3):     
        t.rt(120)          
        t.fd(length)

sierpinski(20, 4)

turtle.mainloop()