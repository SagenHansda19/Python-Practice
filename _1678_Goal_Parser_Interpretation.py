class Solution:
     def interpret(self, command: str) -> str:
          answer = []
          for i in range(len(command)):
               if command[i] == "G":
                    answer.append("G")
               elif command[i] == "(":
                    if command[i+1] == ")":
                         answer.append("o")
                    elif command[i+1] == "a":
                         answer.append("al")
          return "".join(answer)
sol = Solution()
print(sol.interpret("G()(al)")) 