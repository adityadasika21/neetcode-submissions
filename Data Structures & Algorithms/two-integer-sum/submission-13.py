class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = {}

        for i, n in enumerate(nums): 
            required = target - n
            if required in difference_map:
                return [difference_map[required],i]
            
            difference_map[n] = i