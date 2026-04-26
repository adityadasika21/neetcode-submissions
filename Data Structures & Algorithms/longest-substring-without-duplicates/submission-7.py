class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        charSet = set()
        res = 0
        for j in range(len(s)): 
            while s[j] in charSet: 
                charSet.remove(s[l])
                l+= 1
            charSet.add(s[j])
            res = max(res, j - l + 1)

        return res
        