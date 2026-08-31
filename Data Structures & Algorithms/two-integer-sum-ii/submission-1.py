class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        r = len(numbers) - 1
        while i < r:
            sum = numbers[i] + numbers[r]
            if sum == target:
                return [i + 1, r + 1]
            elif sum > target:
                r -= 1
            elif sum < target:
                i += 1
        
            