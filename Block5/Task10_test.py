import Task10

def test(result,*args):
    res=Task10.test(*args)
    if res!=result:
        print('Получен результат '+str(res)+' вместо '+str(result),*args)

test(102,100,1000,2,5)
test(112,108,1000,2,5)
test(100,100,1000,2,7)
test(104,100,1000,6,7)
test(111,110,1000,6,7)