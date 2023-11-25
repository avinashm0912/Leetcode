class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        l = 0
        res = 0
        n = len(s)
        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l = l+1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res
        