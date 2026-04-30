class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffMap = {}

        for i, n in enumerate(nums): 
            
            curDifference = target - n
            if curDifference in diffMap:
                return [diffMap[curDifference], i]

            diffMap[n] = i
        
        return []