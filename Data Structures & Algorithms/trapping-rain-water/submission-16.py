class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        trappedWater = 0
        maxL = 0
        maxR = 0
        i = 0
        while l < r:
            water = min(maxL, maxR) - height[i]
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if water > 0:
                trappedWater += water
            if maxL <= maxR:
                l += 1
                i = l
            else:
                r -= 1
                i = r
            
            
        return trappedWater

