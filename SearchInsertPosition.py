class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return 0
        L, R = 0, len(nums)-1
        while L < R:
            M = (L+R)/2
            if nums[M] < target:
                L = M+1
            else:
                R = M
        return L if nums[L] >= target else L+1
