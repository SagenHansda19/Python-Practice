class Solution:
     def numJewelsInStones(self, jewels: str, stones: str) -> int:
          count = 0
          for i in range(len(jewels)):
               for j in range(len(stones)):
                    if stones[j] == jewels[i]:
                         count += 1
          return count
sol = Solution()
print(sol.numJewelsInStones("aA", "aAAbbbb"))