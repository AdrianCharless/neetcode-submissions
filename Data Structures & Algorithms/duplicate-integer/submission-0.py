class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_list = {}
        for num in nums:
            if num in dupe_list:
                return True
            dupe_list[num] = True

        return False