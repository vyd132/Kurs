def test(N,M,x,y):
    if x<N-x:
        if x<y and x<M-y:
            return x
        elif y<M-y:
            return y
        else:
            return M - y
    elif N-x<y and N-x<M-y:
        return N-x
    elif y<M-y:
        return y
    else:
        return M-y

if __name__=='main':
    N=int(input())
    M=int(input())
    x=int(input())
    y=int(input())
    print(test(N,M,x,y))