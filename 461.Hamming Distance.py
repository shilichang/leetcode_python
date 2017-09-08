x=1
y=4
bin(x)[2:]
bin(y)[2:]
max(len(bin(x)[2:]),len(bin(y)[2:]))


a='%032d' % int(bin(y)[2:])



a='%032d' % int(bin(x)[2:])
b='%032d' % int(bin(y)[2:])
rtype=0
for i in range(32):
    if a[i]!=b[i]:
        rtype+=1

            