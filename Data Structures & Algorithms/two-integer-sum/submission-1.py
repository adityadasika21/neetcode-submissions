class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        seeMap = {}
                
        for i, num in enumerate(nums): 
            differ = target - num

            if differ in seeMap: 
                return [seeMap[differ], i]

            seeMap[num] = i
            
        return -1