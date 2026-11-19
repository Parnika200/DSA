a=[1,1,0,1,1,1,1,0,1,1]
c=0
max=0
for i in a:
    if i==1:
        c+=1
    else:
        c=0
    if c>max:
        max=c
print(max)