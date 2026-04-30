from typing import List

class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
      start = i

      while stack and stack[-1][1] > h:
        index, height = stack.pop()
        max_area = max(max_area, height * (i - index))
        start = index

      stack.append((start, h))

    for pair in stack:
      max_area = max(max_area, (len(heights) - pair[0]) * pair[1])

    return max_area
  
sol = Solution()
heights = [2,1,5,6,2,3]
# heights = [2,1,2]
# heights = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
# heights = [1,4,5,3,2,7,5,3,1]
print(sol.largestRectangleArea(heights))