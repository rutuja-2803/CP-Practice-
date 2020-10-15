#15/10/2020
#jolly jumper problem

sequence=list(map(int,input().split()))
a=[]
for i in range(1,len(sequence)):
    a.append(i)
for i in range(0,len(sequence)):
    if abs(sequence[i]-sequence[i-1]) in set(a):
        flag=1
        pass
    else:
        flag=0
        break
if flag==1:
    print("jolly")
else:
    print("not jolly")