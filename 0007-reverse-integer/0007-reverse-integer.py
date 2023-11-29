class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 0
        sign = 1
        if x < 0:
            sign = -1
            x = x* -1
        while x>0:
            rem = x%10
            s = s*10 +rem
            x = x//10
        if not -2147483648 < s < 2147483647:
            return 0
        return sign * s
        