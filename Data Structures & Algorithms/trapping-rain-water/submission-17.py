class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        trappedWater = 0
        maxR = 0
        maxL = 0
        i = 0
        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            water = min(maxL, maxR) - height[i]
            if water > 0:
                trappedWater += water
            if maxL >= maxR:
                r -= 1
                i = r
            else:
                l += 1
                i = l
            
        return trappedWater
