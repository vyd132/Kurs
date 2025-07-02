n= int(input())

res=0
y=int(input())

for x in range(1,n):
    number=int(input())
    res+=y*number
    y = number

print(res)