def max_area(height:list[int])->int:
    area: int = 0
    left: int = 0
    right:int = len(height) - 1

    while left < right:
        current_area = min(height[left], height[right])  * (right-left)
        if current_area > area:
            area = current_area
        if height[right] > height[left]:
            left += 1
        else:
            right -= 1
    return area

height = [1,1]
a = max_area(height)
print(a)