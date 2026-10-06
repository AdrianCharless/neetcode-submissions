class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        OFFSET = 1000
        count = [0] * 2001
        for num in nums:
            count[num + OFFSET]+=1
        
        for i in range(2000, -1, -1):
            if count[i] > 0:
                k-=count[i]
                if k<= 0:
                    return i - OFFSET

        return -1