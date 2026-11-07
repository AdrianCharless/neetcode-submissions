class Solution:
    def isHappy(self, n: int) -> bool:
        def cycle(num):
            sum = 0
            if num == 1000:
                sum = 1
            elif num > 99:
                hun = num // 100
                sum += hun * hun
                ten = (num - 100 * hun) // 10
                sum += ten * ten
                one = (num - 100 * hun - 10 * ten)
                sum += one * one
            else:
                ten = num // 10
                sum += ten * ten
                one = (num - 10 * ten)
                sum += one * one

            return sum
        num = n
        cycledNums = set()
        cycledNums.add(n)
        while True:
            num = cycle(num)
            print(num)
            if num == 1:
                return True
            elif num in cycledNums:
                return False
            else:
                cycledNums.add(num)

        
