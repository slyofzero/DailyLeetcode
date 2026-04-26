from typing import List

class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stack = []
    output = [0] * len(temperatures)

    for i,temp in enumerate(temperatures):
      while stack and temp > temperatures[stack[-1]]:
        output[stack[-1]] = i-stack[-1]
        stack.pop()

      stack.append(i)

    return output

temperatures = [73,74,75,71,69,72,76,73]
sol = Solution()
print(sol.dailyTemperatures(temperatures))