x=int(input())
p=int(input())
y=int(input())
x*=100
y*=100
c=0
while not x>=y:
    x+=x*p//100
    c+=1

print(c)