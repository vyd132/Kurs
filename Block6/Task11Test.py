import Task11
def test(result,*args):
    res=Task11.test(list(args))
    if res!=result:
        print('Получен результат '+str(res)+' вместо '+str(result)+' параметры',*args)


test(1,1,1,1,2,2)
test(1,1,1,2,2,1)
test(1,1,1,2,2,3,1,1)
test(1,1,2,3,4,1,1,1)

