class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff_map = {}

        for i, n in enumerate(nums):
            
            current_difference = target - n

            if current_difference in diff_map: 
                return [diff_map[current_difference], i]

            diff_map[n] =  i

        return []