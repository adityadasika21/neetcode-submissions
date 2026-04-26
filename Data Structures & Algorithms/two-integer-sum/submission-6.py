class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffs = {}

        for i, n in enumerate(nums): 
            currDif = target - n
            if currDif in diffs: 
                return [diffs[currDif], i]

            diffs[n] = i