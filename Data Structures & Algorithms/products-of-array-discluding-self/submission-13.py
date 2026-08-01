class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preIndexProduct = [1 for i in range(len(nums))]
        postIndexProduct = [1 for i in range(len(nums))]
        for i in range(1, len(nums), 1):
            preIndexProduct[i] = preIndexProduct[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            postIndexProduct[i] = postIndexProduct[i + 1] * nums[i + 1]

        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = preIndexProduct[i] * postIndexProduct[i]
        
        return output

