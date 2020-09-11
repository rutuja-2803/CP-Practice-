#11/9/2020
#trip problem
n=int(input())
amount=[]
for i in range(0,n):
    amount.append(float(input()))
avg=sum(amount)/n
exchange=0
exchange1=0
exchange2=0
exchange3=0
for i in range(0,n):
    if amount[i]<avg:
        exchange1+=avg-amount[i]
    elif amount[i]>avg:
        exchange2+=amount[i]-avg
    elif amount[i]==avg:
        exchange3=0
exchange=exchange1+exchange2+exchange3
print(exchange/2)