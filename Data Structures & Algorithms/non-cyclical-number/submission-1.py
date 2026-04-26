class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit: 
            visit.add(n)
            n = self.sumofSquares(n)
            if n == 1:
                return True
        return False


    def sumofSquares(self, number):
        output = 0
        while number:
            digit = number % 10
            digit = digit ** 2
            output += digit
            number = number // 10
        return output
