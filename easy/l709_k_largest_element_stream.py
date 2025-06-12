import heapq

class KthLargest:
    k:int
    heap: list[int] = []

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums[:]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
    
kthLargest = KthLargest(3, [4, 5, 8, 2])
kthLargest.add(3)
kthLargest.add(5)
kthLargest.add(10)
kthLargest.add(9)
kthLargest.add(4)
print(kthLargest)