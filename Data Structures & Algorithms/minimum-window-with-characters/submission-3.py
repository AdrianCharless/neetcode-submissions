class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, target = {}, {}
        if t == "":
            return ""
        for i in range(len(t)):
            target[t[i]] = target.get(t[i], 0) + 1
        l = 0
        matches = 0
        targetMatches = len(target)
        res = [-1, -1]
        lenRes = float("infinity")
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            
            if s[r] in target and window[s[r]] == target[s[r]]:
                matches += 1
            
            while matches == targetMatches:
                if r - l + 1 < lenRes:
                    res = [l, r]
                    lenRes = r - l + 1
                window[s[l]] -= 1
                if s[l] in target and (window[s[l]] + 1) == target[s[l]]:
                    matches -= 1
                l += 1
        if lenRes != float("infinity"):
            return s[res[0]: res[1] + 1]
        else:
            return ""
                

