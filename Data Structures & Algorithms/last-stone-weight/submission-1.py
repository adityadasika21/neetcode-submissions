class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        newStones = [-x for x in stones]
        heapq.heapify(newStones)

        while len(newStones) > 1: 
            stone1 = heapq.heappop(newStones)
            stone2 = heapq.heappop(newStones)

            if stone2 > stone1: 
                heapq.heappush(newStones ,stone1 - stone2)
                
        newStones.append(0)
        return abs(newStones[0])