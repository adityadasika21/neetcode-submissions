class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        curset, subsetTree = [], []
        self.helper(0, nums, curset, subsetTree)
        return subsetTree

    def helper(self, i, nums, curset, subsetTree):
        if i == len(nums):
            subsetTree.append(curset.copy())
            return 

        curset.append(nums[i])
        self.helper(i + 1 , nums, curset, subsetTree)

        curset.pop()
        self.helper(i + 1 , nums, curset, subsetTree)