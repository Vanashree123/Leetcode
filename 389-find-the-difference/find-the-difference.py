class Solution:

  def findTheDifference(self, s: str, t: str) -> str:
    s_list = list(s)
    for i in t:
      if i not in s_list:
        return i
      s_list.remove(i)