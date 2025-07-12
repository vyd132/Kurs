A= int(input())

a=0
b=1
c=1

while True:
    n=a+b
    a,b=b,n
    c+=1
    if n>A:
        print(-1)
        break
    elif n==A:
        print(c)
        break

