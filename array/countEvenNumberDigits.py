a=[1,23,222,3,444,44]
c=0
for i in a:
    if len(str(i))%2==0:
        c+=1
print("number of even digit numbers",c)