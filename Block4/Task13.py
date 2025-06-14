a=int(input())
b=int(input())
c=int(input())
# d=0
#
# if a==b:
#     d+=1
#
# if a==c:
#     d += 1
#
# if b==c:
#     d += 1
#
# if d==1:
#     d+=1

if a==b and a==c:
    print(3)
elif a==b or a==c or b==c:
    print(2)
else:
    print(0)

