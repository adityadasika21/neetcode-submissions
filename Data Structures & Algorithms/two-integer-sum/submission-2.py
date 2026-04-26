class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cache = {}

        for i,n in enumerate(nums): 
            difference = target - n

            if difference in cache: 
                return [cache[difference], i]

            cache[n] = i

        return -1