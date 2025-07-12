def test(a,b,c,d):
    for number in range(c + (a - c + d - 1) // d*d, b + 1, d):
        return number

if __name__=='main':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())