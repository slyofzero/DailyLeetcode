from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m*n
        mid  = (i+j) // 2

        while i < j:
            row, col = mid // n, mid % n
            
            if target < matrix[row][col]:
                j = mid
            elif target > matrix[row][col]:
                i = mid + 1
            else:
                return True
            
            mid = (i+j) // 2

        return False
    
sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = -3
print(sol.searchMatrix(matrix, target))