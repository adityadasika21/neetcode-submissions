class MedianFinder:

    def __init__(self):
        self.container = []        

    def addNum(self, num: int) -> None:
        self.container.append(num)
        
    def findMedian(self) -> float:
        self.container.sort()
        n = len(self.container)
        if n % 2 == 0 : 
            return float( (self.container[n//2] + self.container[n // 2 - 1]) /2)
        return float( self.container[n//2])
        