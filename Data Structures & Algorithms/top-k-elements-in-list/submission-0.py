class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_freq = {}
        result = []
        for num in nums:
            if num in dict_freq:
                dict_freq[num] += 1
            else:
                dict_freq[num] = 1
        while k > 0:
            most_frequent = max(dict_freq, key=dict_freq.get)
            result.append(most_frequent)
            del dict_freq[most_frequent]  # remove so next iteration finds the next highest
            k -= 1

        return result
            
