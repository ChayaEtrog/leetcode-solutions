class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums) - 1

        while n > 0 and nums[n] <= nums[n - 1]:
            n -= 1

        n -= 1
        if n >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[n]:
                j -= 1

            nums[n], nums[j] = nums[j], nums[n]

        nums[n + 1:] = reversed(nums[n + 1:])


        
        
        
