class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        i = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[i])
                i += 1
            charSet.add(s[r])
            res = max(res, r - i + 1)

        return res