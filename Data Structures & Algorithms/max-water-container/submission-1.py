class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        max_area=0
        for i in range(len(heights)-1):
            for j in range(i, len(heights)):
                min_height=min(heights[i], heights[j])
                area=min_height*(j-i)

                if area>max_area:
                    max_area=area

        return max_area


