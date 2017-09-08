class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=maxLength=0
        usedchar={}
        for i in range(len(s)):
            if  s[i] in usedchar and start<usedchar[s[i]]:
                start=usedchar[s[i]]+1
            else:
                maxLength=max(maxLength,i-start+1)
            usedchar[s[i]]=i

        return maxLength


s='abac'
for i in range(len(s)):
sol=Solution()
sol.lengthOfLongestSubstring('abcde')