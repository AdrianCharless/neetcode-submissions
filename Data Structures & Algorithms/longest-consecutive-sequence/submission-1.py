class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        globalMax = 0
        localMax = 0
        for num in nums:
            localMax = 1
            if (num - 1) not in nums:
                while (num + 1) in numset:
                    localMax += 1
                    num += 1
                if localMax > globalMax:
                    globalMax = localMax

        return globalMax
