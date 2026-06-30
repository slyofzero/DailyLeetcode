from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        mid  = (i+j) // 2

        while i < j:
            if target < nums[mid]:
                j = mid
            elif target > nums[mid]:
                i = mid + 1
            else:
                return mid

            mid = (i+j) // 2

        return -1
    
sol = Solution()
nums = [5]
target = -5
print(sol.search(nums, target))