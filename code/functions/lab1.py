import turtle

t = turtle.Turtle()
t.speed(10)

def sierpinski(length, n):
    if n == 1:
        draw_triangle(length)
    else:
      sierpinski(length, n-1)
      t.rt(120)
      t.fd(length)
      sierpinski(length, n-1)
      t.lt(120)               
      t.fd(length) 
      sierpinski(length, n-1)
      t.fd(length)  
         
def draw_triangle(length):
    t.setheading(180)      
    for i in range(3):     
        t.rt(120)          
        t.fd(length)

sierpinski(50, 3)

turtle.mainloop()