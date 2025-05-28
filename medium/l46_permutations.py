def permute(nums: list[int])->list[list[int]]:    
    # Base case
    if len(nums)==1:
        return [nums]
    
    new_results:list[list[int]]  = []
    for i in range(len(nums)):
        # Probably the remove one is better
        nums_no_i = nums[:i]
        nums_no_i.extend(nums[i+1:])
        results = permute(nums_no_i)
        for result in results:
            result.insert(0, nums[i])
            new_results.append(result)
    return new_results

def permute_online_solution(nums: list[int])->list[list[int]]:
    """
    The main difference is that they go from the back to the front which makes it more efficiently in python
    """
    result = []
    if(len(nums)==1):
        return [nums[:]]
    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = permute_online_solution(nums)
        for perm in perms:
            perm.append(n)
        nums.append(n)
    return result

nums  = [1, 2, 3]
result = permute(nums)

print(result)