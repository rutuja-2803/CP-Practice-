#4/9/2020
#trip problem
n=int(input())
amount=[]
for i in range(0,n):
    amount.append(float(input()))
avg=sum(amount)/n
share1=0
share2=0
for i in range(0,n):
    if amount[i]<avg:
        share1=(avg-amount[i])
    elif amount[i]>=avg:
        share2=amount[i]-avg
if share1<share2:
    print(share1)
else:
    print(share2)
