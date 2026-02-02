class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[right] + nums[left] < 0:
                    left += 1
                
                elif nums[i] + nums[right] + nums[left] > 0:
                    right -= 1
                
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left +=1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1

        return res


            
        