class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        allNine = True
        for num in digits:
            if num != 9:
                allNine = False
                break
        if allNine:
            res = [0] * (len(digits) + 1)
            res[0] = 1
            return res
        i = len(digits) - 1
        carry = 1
        res = [0] * len(digits)
        while i >= 0:
            if (digits[i] + carry) == 10:
                res[i] = 0
                carry = 1
            else:
                res[i] = digits[i] + carry
                carry = 0
            i -= 1
        
        return res

