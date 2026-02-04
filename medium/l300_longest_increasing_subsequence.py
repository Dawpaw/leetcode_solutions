def len_of_list(nums: list[int]) -> int:
    tracker = [1]*len(nums)
    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            if (nums[i] < nums[j]):
                tracker[i] = max(tracker[i], 1 + tracker[j])
    return max(tracker)

if __name__=="__main__":
    a = [10,9,2,5,3,7,101,18]
    a = [0,1,0,3,2,3]
    a = [7,7,7,7,7,7,7]
    res = len_of_list(a)
    print(res)