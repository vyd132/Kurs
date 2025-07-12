n = int(input())
i = 3
if n%2!=0:
    while n%i != 0:
        i += 2
        if i*i>n:
           i=n
    else:
        print(i)
else:
    print(2)
