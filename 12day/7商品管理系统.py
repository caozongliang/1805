print('商品管理系统'.center(40,"*"))
a = []
count = 0
while True:
    fun = int(input('1--添加\n2--删除\n3--改\n4--查\n0--退出\n'))
    if fun == 1:
        b = []
        n = input('请输入商品的名字')
        c = float(input('请输入商品的价格'))
        b.append(n)
        b.append(c)
        a.append(b)
        print(a)

    elif fun ==2:
        n = input('请输入你想删除的商品')
        if n in a:
            a.pop(count)
            print('删除成功')
            count+=1
        else:
            print('没有这个商品')
    elif fun ==3:
        
        e = input('你想修改的商品的名字)
        for n in a:
            if d == n[0]:
                print("1.修改名字")
                print('2.修改价格')
                print('3.修改名字和价格')
                gn = int(input('请选择功能'))
                if gn ==1:
                    e = input('请输入新的名字')
                    n[0]=e
                elif gn == 2:
                    c = int(input('亲输入价格'))
                    n[1]=c
                elif gn == 3:
                    d = input('请输入新名字')
                    c = input('请输入新价格')
                    n[0]=e
                    n[1]=c
        '''
        if d == 1:
            position = a.index(d)
            d = input('请输入新的商品的名字')
            a[position]=d
        elif d ==2:
            position = a.index(d)
            d = float(input('请输入新的价格'))
            a[position]=a.index(d)
        elif d == 3:
            position = a.index(d)
            d = input('请输入新的名字和价格')
            a[position]=a.index(d)
        else:
            print('没有这个商品')
        '''
    elif fun == 4:
        l = input('请输入你想查找的商品')
        for n in a:
            if l == n[0]:
                print("商品名字是%s，价格是%.2f"%(l,n[1]))
            else:
                print('没有这个商品')
    elif fun == 0:
        print('退出')
        break
    print(a)

