accounts = [[1,2,3],[3,2,1]]
max=0
for customer in accounts:
    sum=0
    for money in customer:
        sum=sum+money
    if sum>max:
        max=sum
print(max)
        
        
