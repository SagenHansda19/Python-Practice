class Solution:
     def findPermutationDifference(self, s: str, t: str) -> int:
          n = len(s)
          sum = 0
          for i in range(n):
               check = s[i]
               for j in range(n):
                    if t[j] == check:
                         sum += abs((i+1) - (j+1))
          return sum
sol = Solution()
print(sol.findPermutationDifference("abc", "bac")) 