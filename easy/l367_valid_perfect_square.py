def isPerfectSquare(num: int) -> bool:    
    # Binary search
    left  = 1
    right = num

    while(left<=right):
        mid = (left+right) // 2
        mid_squared = mid * mid
        if(mid_squared>num):
            right = mid - 1 
        elif(mid_squared<num):
            left = mid + 1
        else:
            return True
    return False

num = 321489
print(isPerfectSquare(num))