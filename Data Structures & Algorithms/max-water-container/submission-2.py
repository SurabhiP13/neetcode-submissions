class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        max_area=0
        i,j=0, len(heights)-1
        while i<j:
            min_height=min(heights[i], heights[j])
            area=min_height*(j-i)

            if area>max_area:
                max_area=area

            if heights[i]<heights[j]:
                i+=1
            elif heights[j]<heights[i]:
                j-=1
            else:
                i+=1
                j-=1

        return max_area




