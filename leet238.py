from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    output = [1]
    for num in nums:
      output.append(output[-1] * num)

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
      output[i + 1] = postfix * output[i]
      postfix *= nums[i]

    return output[1:]

nums = [1,2,3,4]
sol = Solution()
print(sol.productExceptSelf(nums))