def test(N,M,x,y):
    if N > M:
        N, M = M, N
    if x >= N / 2:
        x = N - x
    if y >= M / 2:
        y = M - y
    if x < y:
        return x
    else:
        return y

if __name__=='main':
    N=int(input())
    M=int(input())
    x=int(input())
    y=int(input())
    print(test(N,M,x,y))
