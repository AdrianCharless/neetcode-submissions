class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        l = 0
        maxF = 0
        res = 0
        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r], 0) + 1
            maxF = max(maxF, charCount[s[r]])
            if (r - l + 1 - maxF) > k:
                charCount[s[l]] -= 1
                l += 1

            else:
                res = max(res, r - l + 1)

        return res
                

