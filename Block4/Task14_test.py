import Task14


def test(result,*args):
    res=Task14.test(*args)
    if res!=result:
        print('Получен результат '+str(res)+' вместо '+str(result),*args)

test('INF',0,0)
test('NO',6,-2)
test('NO',6,8)
test(7,1,-7)
test(-7,1,7)
test(2,3,-6)
test('NO',0,5)