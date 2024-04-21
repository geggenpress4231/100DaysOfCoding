class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.charProfile(s) == self.charProfile(t)

    def charProfile(self, s: str) -> dict:
        chp = {}
        for char in s:
            if char not in chp:
                chp[char] = 1
            else:
                chp[char] += 1
        return chp
