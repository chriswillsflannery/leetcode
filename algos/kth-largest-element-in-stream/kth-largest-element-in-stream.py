import heapq


class KthLargest:
    # stream means we can keep adding numbers to nums list
    def __init__(self, k: int, nums: List[int]):
        # track top k elements using min heap of size k
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
"""
We can use the builtin heapq which is part of the std lib for python.

Under teh hood the minheap keeps a sorted record of the values in
least to greatest order, so when you pop, you know you're removing the
smallest value, (and the next smallest becomes the new smallest)
and when you push, if the value you pushed is the new
smallest number, the heap will recognize this.
"""