class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        preProd = [1] * len(nums)
        postProd = [1] * len(nums)
        for i in range(len(nums)):
            if i > 0:
                preProd[i] = nums[i - 1] * preProd[i - 1]

        for j in range(len(nums) - 1, -1, -1):
            if j < len(nums) - 1:
                postProd[j] = nums[j + 1] * postProd[j + 1]

        for i in range(len(nums)):
            output[i] = preProd[i] * postProd[i]

        return output