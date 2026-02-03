class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)

        start = [1] * n
        end   = [1] * n

        mul = 1
        for i in range(n):
            start[i] = mul
            mul *= nums[i]

        mul = 1
        for i in range(n - 1, -1, -1):
            end[i] = mul
            mul *= nums[i]

        answer = [1] * n
        for i in range(n):
            answer[i] = start[i] * end[i]

        return answer