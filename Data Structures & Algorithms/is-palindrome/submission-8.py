class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        r = len(s) - 1
        while i < r:
            if s[i].isalnum() == False:
                i += 1
                continue
            if s[r].isalnum() == False:
                r -= 1
                continue
            if s[i].lower() != s[r].lower():
                return False
            else:
                i += 1
                r -= 1
        
        return True
            
            
            
            