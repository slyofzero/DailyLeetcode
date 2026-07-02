from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1

        while i <= j:
            mid = (i+j) // 2

            if nums[mid] >= nums[i]:
                if nums[mid] > nums[j]:
                    i = mid + 1
                else:
                    return nums[i]
            elif nums[mid] <= nums[i]:
                if nums[mid] < nums[j]:
                    j = mid
                else:
                    return nums[j]

        return -1
    
sol = Solution()
nums = [3,4,5,1,2]
print(sol.findMin(nums))