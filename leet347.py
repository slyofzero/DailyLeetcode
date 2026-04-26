from typing import List

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counts = {}
    max_count = 0
    
    for num in nums:
      counts.setdefault(num, 0)
      counts[num] += 1

      if counts[num] > max_count:
        max_count = counts[num]
 
    buckets = [[] for _ in range(max_count)]
    for key in counts:
      buckets[max_count - counts[key]].append(key)

    output = []
    for bucket in buckets:
      output += bucket
      if len(output) >= k:
        return output[:k]

    return output[:k]

sol = Solution()
nums = [1,1,1,2,2,3]
print(sol.topKFrequent(nums, 2))