class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """


n=15
ans=[]
for i in range(n):
    if (i+1)%15==0:
        ans.append("FizzBuzz")
    elif (i+1)%5==0:
        ans.append("Buzz")
    elif (i+1)%3==0:
        ans.append("Fizz")
    else:
        ans.append(str(i+1))