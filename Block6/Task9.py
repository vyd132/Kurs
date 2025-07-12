def test(args):

    a=args.pop(0)
    b1=a
    b2=0
    while a!=0:
        if b1>a:
            b2=b1
            b1=a
        a = args.pop(0)
    return b2


