from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    so_far = {}

    for i, num in enumerate(nums):
      if target - num in so_far:
        return [i, so_far[target - num]]
      
      so_far[num] = i

    return [0,-1]
  
sol = Solution()
nums, target = [2,7,11,15], 9
print(sol.twoSum(nums, target))