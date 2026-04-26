class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = defaultdict(int)

        for n in nums: 
            if n in counter: 
                return n 
            
            counter[n] += 1

        