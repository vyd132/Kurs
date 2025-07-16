def test(args):

    a=args.pop(0)
    b1=10**9
    b2=10**9
    while a!=0:
        if a<b1:
            b2=b1
            b1=a
        elif a<b2:
            b2=a
        a = args.pop(0)
    return b2


# a =int(input())
# b1=10**9
# b2=10**9
# while a!=0:
#     if a<b1:
#         b2=b1
#         b1=a
#     elif a<b2:
#         b2=a
#     a= int(input())
# print(b2)