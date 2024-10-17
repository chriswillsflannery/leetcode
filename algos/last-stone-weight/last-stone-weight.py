class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we can sort first and work with the stones in sorted order
        # ultimately they will all get smashed down to one so original order doesnt matter

        # if we use a max heap we can track stones like:
        # original [2,3,6,2,4]
        # maxHeap { 6,4,3,2,2 }

        # pop 2, apply smash() operation
        # if anything remains add back to maxheap
        # repeat until maxheap only 1 element

        #python doesn't have a standard maxheap so we will use minheap to simualate maxheap
        # to do this we will pretend we are getting the max in a max heap 
        # by converting all numbers to negatives and get the min in a min heap

        stones = [-s for s in stones]
        heapq.heapify(stones) # linear op

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])
        


