def sortArrayByParity(nums: list[int]) -> list[int]:
    right = len(nums)-1
    left = 0

    while (left < right):
        # If values can be exchange
        if(nums[left]%2!=0 and nums[right]%2!=1):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        else:
            if(nums[left]%2==0):
                left += 1
            if(nums[right]%2 == 1):
                right -= 1
    return nums

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Example 2:

# Input: nums = [0]
# Output: [0]

nums = [0,1,2,4]
print(sortArrayByParity(nums))