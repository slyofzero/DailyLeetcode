class Solution:
  def isValid(self, s: str) -> bool:
    if len(s) % 2 != 0:
      return False

    stack = []
    pairs = {"}":"{", "]":"[", ")":"("}

    for bracket in s:
      if bracket in pairs.values():
        stack.append(bracket)
      else:
        if len(stack) == 0 or pairs[bracket] != stack[-1]:
          return False
        stack.pop()

    return len(stack) == 0
  
sol = Solution()
s = "){"
print(sol.isValid(s))