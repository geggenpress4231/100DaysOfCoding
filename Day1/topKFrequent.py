class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1  
            else:
                counter[num] += 1
        
        return sorted(counter, key=counter.get, reverse=True)[:k]
