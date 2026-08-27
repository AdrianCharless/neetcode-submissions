class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbs = set(nums)
        globalMax = 0
        for num in numbs:
            localMax = 1
            if num - 1 not in numbs:
                while num + 1 in numbs:
                    localMax += 1
                    num += 1
                globalMax = max(globalMax, localMax)
        
        return globalMax
                    
