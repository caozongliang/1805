print('*'*20)
print('1----添加')
print('2----删除')
print('3----修改')
print('4----查找')
print('*'*20)

stus = []
while True: 
    fun = int(input("请选择功能：1，2,3,4"))
    if fun ==1:
        name = input("输入名字")
        stus.append(name)
    elif fun == 2:
        name = input("输入要删除的名字")
        if name in stus:
            stus.remove(name)
        else:
            print("查无此人")
    #print(stus)
    elif fun ==3:
        name = input("请输入要修改的名字")
        if name in stus:
            new = input("请输入新名字")
            a = stus.index(name)
            stus[a] = new
            print("修改成功")
        else:
            print("无法执行")
    elif fun == 4:
        name = input("请输入要查找的名字")



    print(stus)
