from typing import List
from collections import defaultdict

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    nums_set = set(nums)
    seqs = defaultdict(list)

    for num in nums_set:
      if num - 1 not in nums_set:
        seqs[num] = [num]
      else:
        seqs[num - 1].extend(seqs[num] + [num])

    print(seqs)

    return 0

sol = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(nums))