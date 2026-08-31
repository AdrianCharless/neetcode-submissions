class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortNum = sorted(nums)
        # [-4,-1,-1,0,1,2]
        res = []
        for index, num in enumerate(sortNum):
            if index != 0 and num == sortNum[index - 1]:
                continue
            l = index + 1
            r = len(nums) - 1
            while l < r:
                sum = sortNum[l] + sortNum[r]
                if sum + num == 0:
                    res.append([num, sortNum[l], sortNum[r]])
                    l += 1
                    while sortNum[l] == sortNum[l - 1] and l < r:
                        l += 1
                    
                elif sum + num > 0:
                    r -= 1
                elif sum + num < 0:
                    l += 1
        return res

