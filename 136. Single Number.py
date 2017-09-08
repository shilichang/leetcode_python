class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

nums=[1,2,3,1,2]
for i in range(len(nums)):
    if nums.count(nums[i])==1:
        return nums[i]