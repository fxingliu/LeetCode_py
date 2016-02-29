class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.quickSort(nums, 0, len(nums)-1)
        return nums[-k]
        
    def quickSort(self, nums, left, right):
        pivot, L, R = nums[left+(right-left)/2], left, right
        while L <= R:
            while nums[R] > pivot: R -= 1
            while nums[L] < pivot: L += 1
            if L <= R: nums[L], nums[R], L, R = nums[R], nums[L], L+1, R-1
        if L < right: self.quickSort(nums, L, right)
        if R > left: self.quickSort(nums, left, R)
