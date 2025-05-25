def twoSum(nums: list[int], target: int) -> list[int]:
        points = {}

        for i, val in enumerate(nums):
            needed = target - val
            if needed in points:
                return [points[needed], i]
            points[val] = i
        
        return []




nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))