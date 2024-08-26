class Solution:
     def minimumOperations(self, nums: list[int]) -> int:
          operations = 0
          for num in nums:
               remainder = num % 3
               if remainder == 1:
                    operations += 1
               elif remainder == 2:
                    operations += 1
          return operations
sol = Solution()
nums = [3,6,9]
print(sol.minimumOperations(nums))