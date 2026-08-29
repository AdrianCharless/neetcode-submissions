class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = len(temperatures)
        stack = []
        result = [0] * days
        for index, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = index - stackIndex
            stack.append((temp, index))
    
        return result