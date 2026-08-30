class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedCars = [[position[i],speed[i]] for i in range(len(position))]
        sortedCars.sort(key= lambda x: x[0])
        stack = []
        for position, speed in sortedCars:
            timeRemaining = (target - position) / speed
            stack.append((position, speed, timeRemaining))
        fleets = 0
        while stack:
            position, speed, time = stack.pop()
            if stack and time >= stack[-1][2]:
                positionStack, speedStack, timeStack = stack.pop()
                stack.append((positionStack, speedStack, time))
            else:
                fleets += 1
            
        return fleets

