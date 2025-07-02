a = int(input())
b = int(input())

if a<b:
    for number in range(a, b + 1):
        print(number, end=' ')
else:
    for number in range(a, b-1,-1):
        print(number, end=' ')
