import Task11

# assert Task11.test(23,52,8,43)==8
# assert Task11.test(23,52,8,45)==7

def test(result,*args):
    res=Task11.test(*args)
    if res!=result:
        print('Получен результат '+str(res)+' вместо '+str(result),*args)

test(8,23,52,8,43)
test(7,23,52,8,45)
test(7,23,52,8,7)
test(7,23,52,16,8)

test(8,52,23,8,43)
test(7,52,23,8,45)
test(7,52,23,8,7)
test(7,52,23,16,8)