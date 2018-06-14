#***
xs = ''
list = []
while True:
    gn = int(input("请选择功能：1、添加 2、删除"))
    if gn == 1:
        name = input("请输入要添加的名字")
        a = xs.find(name)
        if a != -1:
            print("已有")
        else:
            list.append(name)
            
            print("添加成功")
            xs+=name
    elif gn == 2:
        name = input("请输入要删除的名字")
        a = xs.find(name)
        if a != -1:
            list.remove(name)
            print("成功删除%s"%name)
        else:
            print("没有这个人")
    print("统计学生姓名：%s"%list)
