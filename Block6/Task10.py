def test(args):
    a = args.pop(0)
    b1=0
    b2=0
    num=0
    while a!=0:
        if b1!=0 and b2!=0 and b1>b2 and b1>a:
            num+=1
        if b1!=0:
            b2=b1
        b1=a
        a=args.pop(0)
    return num