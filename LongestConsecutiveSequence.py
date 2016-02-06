class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lcs = 0
        nums = set(nums)
        for begin in nums:
            if begin-1 in nums: 
                continue
            end = begin+1
            while end in nums:
                end += 1
            lcs = max(lcs, end-begin)
        return lcs
        
