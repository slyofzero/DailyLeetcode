class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    
    char_count = [0] * 26
    
    for i in range(len(s)):
      char_count[ord(s[i]) - ord("a")] += 1
      char_count[ord(t[i]) - ord("a")] -= 1

    for count in char_count:
      if count != 0:
        return False

    return True

  # def isAnagram(self, s: str, t: str) -> bool:
  #   char_count = {}
    
  #   for char in s:
  #     char_count.setdefault(char, 0)
  #     char_count[char] += 1

  #   for char in t:
  #     if char not in char_count or char_count[char] <= 0:
  #       return False
  #     char_count[char] -= 1

  #   return sum(char_count.values()) == 0

s = "rat"
t = "car"
sol = Solution()
print(sol.isAnagram(s, t))