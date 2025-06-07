a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

if a>b and a>c:
    min1=b
    min2 = c
elif b>a and b>c:
    min1 = a
    min2 = c
else:
    min1 = a
    min2 = b

if min1<min2:
    min_first=min1
    min_second = min2
else:
    min_first = min2
    min_second = min1

if (d>=min1 and e>=min2) or (d>=min2 and e>=min1):
    print('YES')
else:
    print('NO')