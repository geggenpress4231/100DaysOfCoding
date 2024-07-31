

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAllBananas(k):
            total_hours = sum(ceil(pile / k) for pile in piles)
            return total_hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if canEatAllBananas(mid):
                right = mid
            else:
                left = mid + 1

        return left

