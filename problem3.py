#SOCK MERCHANT PROBLEM
#18/09/2020
n=int(input())
ar= input().split()
value=0
for i in set(ar):
	value += ar.count(i) // 2
print(value)



