class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0 
        end = len(numbers) - 1

        while start < end:
            add = numbers[start] + numbers[end] 
            if add == target:
                return [start+1, end+1]
            
            elif add < target:
                start += 1

            else:
                end -=1
        
