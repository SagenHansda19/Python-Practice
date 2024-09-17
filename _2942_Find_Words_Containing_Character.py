class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
          ans = []
          for s in range(len(words)):
               if x in words[s]:
                    ans.append(s)
          return ans
sol = Solution()
words = ["leet","code"]
x = "e"
print(sol.findWordsContaining(words,x))