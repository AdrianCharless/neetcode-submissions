class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validRate(piles, h, rate):
            dayCount = 0
            for num in piles:
                days = num // rate
                if num % rate > 0:
                    days += 1
                dayCount += days
            return (dayCount <= h)
        
        l = 1
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            if validRate(piles, h, mid):
                r = mid
            else:
                l = mid + 1
                    
        return l