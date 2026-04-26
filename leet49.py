from typing import List

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    groups = {}

    for string in strs:
      char_counts = [0] * 26
      
      for char in string:
        char_counts[ord(char) - ord("a")] += 1

      string_map = tuple(char_counts)
      groups.setdefault(string_map, [])
      groups[string_map].append(string)

    return list(groups.values())
        
strs = ["bdddddddddd","bbbbbbbbbbc"]
sol = Solution()
print(sol.groupAnagrams(strs))