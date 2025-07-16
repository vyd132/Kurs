import Task10
def test(result,*args):
    res=Task10.test(list(args))
    if res!=result:
        print('Получен результат '+str(res)+' вместо '+str(result)+' параметры',*args)

test(1,7,8,7,0)
test(0,0)
test(0,8,0)
test(0,7,8,0)
test(0,7,7,8,0)
test(0,7,6,7,0)
test(0,7,7,7,0)
test(3,7,8,7,6,9,5,8,7,9,9,7,0)