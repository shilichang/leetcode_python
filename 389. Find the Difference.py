s = "abbcd"
t = "abcd"
list(s)&list(t)

for i in range(min(len(s),len(t))):
    if s[i]!=t[i]:
import collections
list(collections.Counter(t) - collections.Counter(s))[0]        