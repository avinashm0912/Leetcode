class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i in range(0,len(nums)):
            value = nums[i]
            difference = target - value
            if value not in d:
                d[difference] = i
            else:
                current_index = i
                prev_index = d[value]
                return [prev_index, current_index]