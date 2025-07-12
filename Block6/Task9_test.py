import Task9

def test(result,*args):
    res=Task9.test(list(args))
    if res!=result:
        print('Получен результат '+str(res)+' вместо '+str(result)+' параметры',*args)

test(2,1,2,3,4,0)
test(2,1,2,0)
test(1,1,1,0)
test(2,4,3,2,1,0)
test(2,4,1,3,2,0)
test(1,4,1,1,2,0)
test(1,1,1,4,2,0)
test(1,4,2,1,1,0)