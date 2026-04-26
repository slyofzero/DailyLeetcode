from typing import List

class Solution:
  def maxArea(self, height: List[int]) -> int:
    l,r = 0, len(height)-1
    max_vol = 0

    while r > l:
      new_vol = min(height[l], height[r]) * (r-l)
      max_vol = max(max_vol, new_vol)

      if height[l] < height[r]:
        l += 1
      else:
        r -= 1

    return max_vol
  
sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))