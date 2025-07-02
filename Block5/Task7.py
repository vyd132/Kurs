n= int(input())

fact=1
res=0

for number in range(1,n+1):
    fact *= number
    res += fact

print(res)