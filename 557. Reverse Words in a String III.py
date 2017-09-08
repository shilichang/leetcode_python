Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

s="Let's take LeetCode contest"
r=[]
for i in range(len(s.split(' '))):
    r.append(s.split(' ')[i][::-1])
return ' '.join(r)