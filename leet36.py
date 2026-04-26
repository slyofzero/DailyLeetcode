from typing import List

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    row_counts = [[False] * 9 for _ in range(9)]
    col_counts = [[False] * 9 for _ in range(9)]
    grid_counts = [[False] * 9 for _ in range(9)]

    for i in range(9):
      for j in range(9):
        item = board[i][j]
        if item == ".":
          continue
        item_index = int(item) - 1

        grid_index = 3 * (i // 3) + (j // 3)

        if (
          row_counts[i][item_index]  
            or col_counts[j][item_index] 
            or grid_counts[grid_index][item_index]
          ):
          return False
        
        row_counts[i][item_index] = True
        col_counts[j][item_index] = True
        grid_counts[grid_index][item_index] = True
 
    return True

board = [
  [".",".",".",".","5",".",".","1","."],
  [".","4",".","3",".",".",".",".","."],
  [".",".",".",".",".","3",".",".","1"],
  ["8",".",".",".",".",".",".","2","."],
  [".",".","2",".","7",".",".",".","."],
  [".","1","5",".",".",".",".",".","."],
  [".",".",".",".",".","2",".",".","."],
  [".","2",".","9",".",".",".",".","."],
  [".",".","4",".",".",".",".",".","."]
  ]

sol = Solution()
print(sol.isValidSudoku(board))