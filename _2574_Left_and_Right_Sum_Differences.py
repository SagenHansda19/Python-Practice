class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        n = len(nums)
        leftsum = [0] * n
        rightsum = [0] * n
        answer = [0] * n
        leftsum[0] = 0
        rightsum[n-1] = 0
        for i in range(1,n,1):
            leftsum[i] = leftsum[i-1] + nums[i-1]
        for i in range(n-2,-1,-1):
            rightsum[i] = rightsum[i+1] + nums[i+1]
        for i in range(n):
            answer[i] = abs(leftsum[i] - rightsum[i])
        return answer
sol = Solution()
print(sol.leftRightDifference([10,4,8,3]))  # [15,1,11,22]
