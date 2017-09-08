class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        


findNums=[4]
nums=[1,4,3,9,7]
ans=[]
for i in range(len(findNums)): 
    if findNums[i]==sorted(nums[nums.index(findNums[i]):])[-1]:
        ans.append(-1)
    else:
        for j in range(len(nums[nums.index(findNums[i]):])):
            if nums[nums.index(findNums[i]):][j]>findNums[i]:
                ans.append(nums[nums.index(findNums[i]):][j])
                break
return ans
a=[3,2,1,4,5]
