class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        total = sum(nums)
        pre_sum = 0
        res = [0]*n
        for i in range(n):
            total -= nums[i]
            left = i*nums[i] - pre_sum
            right = total - (n-i-1)*nums[i]
            pre_sum += nums[i]
            res[i] = left + right
        return res