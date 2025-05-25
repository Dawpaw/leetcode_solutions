def searchRange(nums: list[int], target: int) -> list[int]:

    smallest = binary_search(target, nums, search_left=True)
    largest = binary_search(target, nums, search_left=False)

    return [smallest, largest]

def binary_search(target, nums: list[int], search_left:bool):
    left = 0
    right = len(nums)-1
    i = -1

    while(left <= right):
        mid  = (right + left) // 2
        if(target > nums[mid]):
            left = mid + 1
        elif(target < nums[mid]):
            right = mid - 1
        else: # target == mid
            i = mid
            if(search_left):
                right = mid - 1
            else:
                left = mid +1
    return i




nums = [5,7,7,8,8,8,10]
target = 8

print(searchRange(nums, target))