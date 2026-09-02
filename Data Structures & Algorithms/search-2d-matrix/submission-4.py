class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # 3
        n = len(matrix[0]) # 4
        l = 0
        r = m * n - 1
        while l < r:
            mid = (l + r) // 2 # 5 - 11
            mn = mid % n # 1
            mm = mid // n # 1
            if matrix[mm][mn] == target:
                return True
            elif matrix[mm][mn] > target:
                r = mm * n + mn - 1
            else:
                l = mm * n + mn + 1
        mid = (l + r) // 2
        mn = mid % n
        mm = mid // n
        if matrix[mm][mn] == target:
            return True
        else:
            return False
