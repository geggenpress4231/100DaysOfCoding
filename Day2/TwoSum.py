class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(0,len(nums)):
            #print(target-nums[i])
            if target-nums[i] in map:
                return (i,map[target-nums[i]])
            map[nums[i]]=i
            #print(map)
        return [0,0]        

        