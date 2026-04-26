from typing import List

class Solution:
  def trap(self, height: List[int]) -> int:
    if len(height) <= 2:
      return 0

    total_area = 0
    l,r = 0,len(height)-1
    max_l = height[0]
    max_r = height[-1]
    i = 1

    while r > l:
      if max_l <= max_r:
        l += 1
        total_area += max(0, max_l - height[l])
        max_l = max(max_l, height[l])
      else:
        r -= 1
        total_area += max(0, max_r - height[r])
        max_r = max(max_r, height[r])

    return total_area
  
sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,3]
# height = [4,2,0,3,2,5]
# height = [5,4,2,1,2,0]
# height = [5,4,2,1,3,0]
# height = [5,4,2,1,5,0]
# height = [9,8,2,6]
print(f"Answer - {sol.trap(height)}")