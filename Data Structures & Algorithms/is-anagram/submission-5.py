class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count = {}
        if len(s) != len(t):
            return False
        for l in s:
            letter_count[l] = letter_count.get(l, 0) + 1
        for tl in t:
            if letter_count.get(tl, 0) > 0:
                letter_count[tl] -= 1
            else: 
                return False
        return True