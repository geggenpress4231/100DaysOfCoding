class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen=0
        left=0
        charMap={}
        for right in range(len(s)):
            if s[right] in charMap:
                charMap[s[right]]+=1
            else:
                charMap[s[right]]=1
            while(max(charMap.values())>1):
                if charMap[s[left]]==1:
                    del(charMap[s[left]])
                else:
                    charMap[s[left]]-=1
                left+=1

            maxLen=max(maxLen,right-left+1)
        return maxLen