
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
nums = [[1,2], [3,4]]

r=1
c=4
temp=[]
ans=[]
if len(nums)*len(nums[0])!=r*c:
    return nums
else:
temp=[]
for i in range(len(nums)):
    for j in range(len(nums[0])):
        temp.append(nums[i][j])
for m in range(r):
    ans.append(temp[m*c:(m+1)*c])