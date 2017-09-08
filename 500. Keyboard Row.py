class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
words=["Hello", "Alaska", "Dad", "Peace"]
line1=set('qwertyuiop')
line2=set('asdfghjkl')
line3=set('zxcvbnm')
ans=[]
for word in words:
    temp=set(word.lower())
    if temp & line1==temp:
        ans.append(word)
    if temp & line2==temp:
        ans.append(word)
    if temp & line3==temp:
        ans.append(word)        
return ans                