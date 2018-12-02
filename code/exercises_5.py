epsilon = .0001
a = 4      #number you are taking the sqrt of
x = 3      #estimate of answer

while True:
    print(x)
    y = (x + a/x) / 2
    if abs(y-x) < epsilon:
        break
    x = y
    
    
 