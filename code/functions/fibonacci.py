# def fibonacci(n):
#     """Calculate Fibonacci numbers"""
#     if n <= 1:
#         return n
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))

fibcache = {}

def fibonacci(n):
    if n not in fibcache.keys():
        fibcache[n] = _fibonacci(n)
    return fibcache[n]

def _fibonacci(n):
    """Calculate Fibonacci numbers"""
    if n <= 1:
        return n
    else:
        fib = fibonacci(n-1) + fibonacci(n-2)
        return fib

# built in caching      
# def fibonacci(n):
#     """Calculate Fibonacci numbers"""
#     if n in fibcache.keys():
# 	    return fibcache[n]
#     if n <= 1:
#         fibcache[n] = n
#         return n
#     else:
#         fib = fibonacci(n-1) + fibonacci(n-2)
#         fibcache[n] = fib
#         return fib
      
fibonacci_length = 90
for num in range(fibonacci_length):
    print(fibonacci(num))
    
