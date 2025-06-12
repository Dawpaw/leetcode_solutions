def fib(n: int) -> int:
    if (n<2):
        return n
    
    f1 = fib(n-1)
    f2 = fib(n-2)
    return f2 + f1

a = fib(4)
print(a)