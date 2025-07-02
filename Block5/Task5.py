a = int(input())
b = int(input())

for number in range(a+(a%2),b+1,2):
    print(number,end=' ')