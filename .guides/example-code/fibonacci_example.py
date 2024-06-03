fibcache = {} #dictionary of Fibonacci numbers

def fibonacci(n):
    """Check to see if a Fibonacci number has been calculated (in the dictionary).
    If not, add it to the dictionary and return it.
    If yes, return the number from the dictionary."""
    if n not in fibcache.keys():
        fibcache[n] = _fibonacci(n)
    return fibcache[n]

def _fibonacci(n):
    """Calculate Fibonacci number"""
    if n <= 1:
        return n
    else:
        fib = fibonacci(n-1) + fibonacci(n-2)
        return fib
      
fibonacci_length = 90
for num in range(fibonacci_length):
    print(fibonacci(num))
    
