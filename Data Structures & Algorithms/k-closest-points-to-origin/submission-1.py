class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        newPoints = []
        for point in points: 
            x,y = point 
            distance = x ** 2 + y ** 2
            newPoints.append([distance, x, y])

        heapq.heapify(newPoints)

        res = []

        while k != 0: 
            point = heapq.heappop(newPoints)
            res.append([point[1],point[2]])
            k-=1

        return res