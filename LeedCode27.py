class Solution(object):
    def removeElement(self, nums, val):
        k = len(nums)
        i = 0
        while i < k:
            if nums[i] == val:
                nums[i] = nums[k-1]
                k -= 1
            else:
                i += 1
        return k
