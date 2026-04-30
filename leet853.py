from typing import List

class Solution:
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    cars = sorted(zip(position, speed))
    stack = []

    for car in cars:
      cur_pos, cur_speed = car
      time = (target - cur_pos) / cur_speed

      while stack and stack[-1] <= time:
        stack.pop()

      stack.append(time)
    
    return len(stack)

# testcase = (12, [10,8,0,4,3], [1,3,1,1,3])
# testcase = (31, [5,26,18,25,29,21,22,12,19,6], [7,6,6,4,3,4,9,7,6,4])
testcase = (21, [1,15,6,8,18,14,16,2,19,17,3,20,5], [8,5,5,7,10,10,7,9,3,4,4,10,2])
sol = Solution()
print(sol.carFleet(*testcase))