from typing import List

class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    operators = ["+","-","*","/"]

    for token in tokens:
      if token in operators:
        b = int(stack.pop())
        a = int(stack.pop())

        if token == "+":        
          stack.append(a + b)
        elif token == "-":
          stack.append(a - b)
        elif token == "*":
          stack.append(a * b)
        elif token == "/":
          stack.append(a / b)
      else:
        stack.append(token)

    return int(stack[-1])
  
sol = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(tokens))