def search_insert(nums:list[int], target: int) -> int:
    # It is just typical binary search
    r = len(nums)
    l = 0
    m = -1
    while(l<r):
        m = (r+l)//2
        if(nums[m]>=target):
            r = m
        else:
            l = m + 1
    return l

nums = [1,3,5,6] 
target = 7

a = search_insert(nums, target)
print(a)


# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

