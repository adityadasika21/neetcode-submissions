class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) -1
        ans = -1

        while l < r: 

            vol = (r - l) * min(heights[l], heights[r])

            ans = vol if vol > ans else ans

            if heights[l] < heights[r ]:
                l += 1
                continue
            
            if heights[r ] <= heights[l]:
                r -= 1
                continue

        return ans