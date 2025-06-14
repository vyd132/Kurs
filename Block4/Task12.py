a=int(input())
b=int(input())
c=int(input())

# if a>b:
#     d=a
# else:
#     d=b
# if d>c:
#     print(d)
# else:
#     print(c)

if b>c:
    b,c=c,b
if a<c:
    a,c=c,a

print(a)
