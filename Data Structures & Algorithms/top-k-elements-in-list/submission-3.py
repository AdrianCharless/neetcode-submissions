class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[]for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num in count:
            freq[count[num]].append(num)
        length = len(freq) - 1
        res = []
        while length > 0:
            for num in freq[length]:
                res.append(num)
                if len(res) == k:
                    return res
            length -= 1
                

