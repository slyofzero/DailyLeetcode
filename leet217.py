from evaluator import evaluate_cases
from typing import List

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    items = set()
    
    for num in nums:
      if num in items:
        return True

      items.add(num)
    return False
  
sol = Solution()
tests = [([1,2,3,1], False)]

evaluate_cases(tests, sol.containsDuplicate)
