def isPalindrome(x: int) -> bool:
    num_string = str(x)

    left = 0
    right = len(num_string) - 1

    while(left < right):
        if num_string[left] != num_string[right]:
            return False
        left += 1
        right -= 1
    return True

x = 10001
print(isPalindrome(x))

