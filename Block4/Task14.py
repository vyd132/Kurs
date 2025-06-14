def test(a,b):
    if a==0 and b==0:
        return 'INF'
    if a==0 or abs(b)%a!=0 :
        return 'NO'
    return -b//a

if __name__=='main':
    a = int(input())
    b = int(input())