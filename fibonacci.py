def Fibonacci(n):
    if n < 0:
        raise Exception("bad input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def factorial(x):
    factorial = 1
    for i in range(1,x+1):
        factorial = factorial * 1
    return factorial