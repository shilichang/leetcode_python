nums=[1,0,1,1,0,1]
count=0
ans=0
for num in nums:
    if num==1:
        count+=1
        ans=max(ans,count)
    else:
        count=0
    return ans