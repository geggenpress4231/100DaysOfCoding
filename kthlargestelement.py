import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums[:k]
        heapq.heapify(minHeap)

        for i in range(k,len(nums)):
            if nums[i]>minHeap[0]:
                heapq.heapreplace(minHeap, nums[i])

        return minHeap[0]       

        