class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        preProd = [1] * len(nums)
        postProd = [1] * len(nums)
        for i in range(len(nums)):
            j = i - 1
            while j >= 0:
                preProd[i] *= nums[j]
                j -= 1
            j = i + 1
            while j in range(len(nums)):
                postProd[i] *= nums[j]
                j += 1
        for i in range(len(nums)):
            output[i] = preProd[i] * postProd[i]

        return output