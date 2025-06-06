def rec_pow(x:float, n:int) -> float:
    if n == 0:
        return 1.0
    
    if(n%2!=0): 
        return x * rec_pow(x, n-1)

    temp =  rec_pow(x, n//2)
    return temp * temp


def my_pow(x:float, n:int) -> float:
    flip = False
    if (n<0):
        n = -1 * n
        flip = True
    temp = rec_pow(x, n)
    return 1 / temp if flip else temp

a = my_pow(2.0, -2)
print(a)