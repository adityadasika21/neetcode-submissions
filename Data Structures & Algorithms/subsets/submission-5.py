class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        curSet , subSets = [], []
        self.helper(0, nums, curSet, subSets)
        return subSets

    def helper(self, curIdx, nums, curSet, subSets): 
        if curIdx >= len(nums): 
            subSets.append(curSet.copy())
            return

        curSet.append(nums[curIdx])
        self.helper(curIdx+ 1, nums, curSet, subSets)

        curSet.pop()
        self.helper(curIdx +1 , nums, curSet, subSets)