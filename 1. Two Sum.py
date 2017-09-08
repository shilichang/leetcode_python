class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}          
        for i in range(len(nums)):
            if nums[i] in dict:
                return[dict[nums[i]],i]
            else:
                dict[target-nums[i]]=i





target=28


nums=[-1,-2,-3,-4,-5]
target=-8

nums=[0,3,4,0]
target=0

nums=[3,2,4]
target=6


sol=Solution()
sol.twoSum(nums,target)