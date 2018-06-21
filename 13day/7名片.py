list = []
print("个人名片".center(50,' '))
while True:
    print("1.添加名片".center(50,' '))
    print("2.查找名片".center(50,' '))
    print("3.修改名片".center(50,' '))
    print("4.删除名片".center(50,' '))
    print("5.退出".center(50,' '))
    
    a = int(input("请选择功能"))
    if a == 1:#增
        ren = {}
        name = input("请输入姓名")
        sex = input("请输入性别")
        job = input("请输入职业")
        sjh = input("请输入联系电话")
        ren["name"]=name
        ren["sex"]=sex
        ren["job"]=job
        ren["sjh"]=sjh
        list.append(ren)
        print(list)
    elif a == 2:
        name = input("请输入查找人姓名")
        for i in list:#字典
            #print(i)
            if name == i["name"]:        
                print("姓名:%s\n性别:%s\n职业:%s\n电话:%s\n"%(i["name"],i["sex"],i["job"],i["sjh"]))
            else:
                print("查无此人")
    elif a == 3:
        x = {}
        xg = input("请输入被修改人名字")
        name = input("请输入新的名字")
        sex = input("请输入性别")
        job = input("请输入职业")
        sjh = input("请输入联系电话")
        x["name"]=name
        x["sex"]=sex
        x["job"]=job
        x["sjh"]=sjh
        for i in list:
            if xg == i["name"]:                    
                i.update(x)
                print("修改成功")
                print(list)
    elif a == 4:
        sc = input("输入名字")
        for i in list:
            if sc == i["name"]:
                i.clear()
    elif a == 5:
        break
