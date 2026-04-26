from typing import List

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l,r = 0, len(numbers) - 1

    while r > l:
      p_sum = numbers[l] + numbers[r]

      if p_sum > target:
        r -= 1
      elif p_sum < target:
        l += 1
      else:
        return [l+1,r+1]

    return [0,-1]
  
sol = Solution()
numbers = [2,7,11,15]
target = 9
print(sol.twoSum(numbers, target))