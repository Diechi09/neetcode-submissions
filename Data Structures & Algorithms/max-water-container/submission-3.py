class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        biggest = 0

        while l < r:
            distance = r - l
            small = min(heights[l], heights[r])
            area = small * distance
            biggest = max(area, biggest)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return biggest