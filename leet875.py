from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r) // 2
            hours_needed = sum(math.ceil(pile / k) for pile in piles)
            
            if hours_needed <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
            
        return res
    
sol   = Solution()
piles = [30,11,23,4,20]
h     = 5
print(sol.minEatingSpeed(piles, h))