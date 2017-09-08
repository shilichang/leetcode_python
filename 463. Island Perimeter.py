class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """


grid=[[0,1,0,0], 
      [1,1,1,0], 
      [0,1,0,0],
      [1,1,0,0]]
ans=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]==1:
            ans=ans+4
            print(i,j,ans)
            if i-1>=0 and grid[i-1][j]==1:
                ans-=2
                print(i,j,ans)
            if j-1>=0 and grid[i][j-1]==1:
                ans-=2
                print(i,j,ans)
        else:
            pass