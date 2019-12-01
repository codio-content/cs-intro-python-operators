def return_int(num1, num2):
    """Return the floor division of num1 divided by num2"""
    return(num1 // num2)
  
def return_float(num1, num2):
    """Return num1 divided by num2"""
    return(num1 / num2)
  
def return_string(string):
    """Return the value of string appended to 'Hello` """
    return("Hello {}".format(string))
  
print(return_int(10, 3))
print(return_float(10, 3))
print(return_string(" friend"))