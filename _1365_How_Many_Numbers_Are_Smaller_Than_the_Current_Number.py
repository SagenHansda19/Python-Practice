class Solution:
     def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
          n = len(nums)
          answer = [0] * n
          count = 0
          for i in range(n):
               for j in range(n):
                    if j != i and nums[j] < nums[i]:
                         count+=1
               answer[i] = count
               count = 0
          return answer
sol = Solution()
print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))