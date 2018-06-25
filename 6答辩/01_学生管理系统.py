list = []



#注册账号函数申明
def register():
    import random
    import time
    while True:
        print("学生管理系统".center(50,"*"))
        print("*"*56)
        print("请输入手机号")
        account = input("请输入手机号:\n".center(50," "))
        if len(account) == 11 and account.isdigit() == True and account.startswith("1") == True:
            aaa = random.randint(1000,9999)
            print("正在发送验证码....".center(50," "))
            print("")
            time.sleep(3)
            print("您正在用手机号码进行注册学生管理账号,验证码为:%s"%aaa)
            print("*"*50)
            sss = int(input("请输入验证码"))
            if sss == aaa:
                print("注册成功")
                break
            else:
                print("输入有误!")
#申明登录函数*****然后嵌套函数*************************************
def logo():
    print("学生管理系统".center(50,"*"))
    print("*"*56)
    print("欢迎使用学生管理系统".center(50," "))
    print('')
def ll_1():   #登录原有内部账号 
    
    print("请登录:".center(53," "))
    zhang_hao = "123456"#定义一个账号
    mi_ma = "654321"#定义密码
    for i in range(3):#循环三次,输入正确停止,最多输入三次
        account = input("请输入账号:")
        flag = False
        password = input("请输入密码:")
        flag = True
        if (account == zhang_hao) and (password == mi_ma):
            print("登录成功".center(50,"*"))    
            break
        else:
            print("输入有误,请重新输入")
            if i == 2:
                print("账号密码无效,请注册后登录")
                register()
#用户界面函数******************************************
def ui():    
    print("\t1.添加学员资料",end="\t\t")
    print("2.查看学员资料")
    print("")
    print("\t3.修改学员资料",end="\t\t")
    print("4.删除学员资料")
    print("")
    print("\t5.打印所有学员资料",end="\t ")
    print("6.退出系统")
#添加资料函数****************************************
def add():    
    group = {}
    student_id = input("输入学号:")
    student_name = input("输入姓名:")
    student_sex = input("输入性别:")
    student_score = input("输入成绩")
    student_time = input("输入入学时间")
    group["ID"]=student_id
    group["name"]=student_name
    group["sex"]=student_sex
    group["score"]=student_score
    group["time"]=student_time
    list.append(group)
    print("添加成功")

#查看资料函数***************************
def cat():
        flag = True
        for i in list:
            a = input("请输入学员姓名")
            if a == i["name"]:
                print("姓名:%s"%i["name"])
                print("性别:%s"%i["sex"])
                print("学号:%s"%i["ID"])
                print("成绩:%s"%i["score"])
                print("入学时间:%s"%i["time"])
                flag = False        
                break
        if flag == True:    
            print("查无此人,请添加后查询!")
#修改资料函数*********************************
def change():
    flag = False
    for i in list:
        a = input("请输入学员姓名")
        if a == i["name"]:
            flag = True
            b = int(input("选择修改项目:1.姓名,学号和性别 2.成绩 3.入学时间"))
            if b == 1:
                name = input("输入新的名字")
                sex = input("输入性别")
                ID = input("输入新学号")
                i["name"] = name
                i["sex"] = sex
                i["ID"]  = ID
            elif b == 2:
                score = input("输入新成绩")
                if score.isgidit() == True:
                    i["score"] = score
                else:
                    print("输入有误")
            elif b == 3:
                time = input("输入入学时间")
                i["time"] = time
            else:
                print("输入有误")

    if flag == False:
        print("查无此人")
#删除资料函数***********************************
def del_q():
    n = input("输入删除人员姓名")
    flag = False
    for position,i in enumerate(list):
        if i['name'] == n:
            list.pop(position)
            print("删除成功")
            flag = True
    if flag == False:
        print("查无此人")
#打印资料函数申明********************************
def print_all():
    print("姓名\t 学号\t 性别\t 成绩\t 入学时间\t")
    for i in list:
        print(" "+i["name"]+"\t "+i["ID"]+"\t "+i["sex"]+"\t "+i["score"]+"\t "+i["time"]+"\t")
        
        
            
logo()#调用登录函数,注册
ll = int(input("1.登录\t2.注册".center(50," ")))
if ll == 1:
    a = ll_1()
if ll == 2:
    register()
while True:
    ui()#登录成功后调出用户选择界面
    function = int(input("选择功能"))
    if function == 1:#如果用户选择添加
        add()#调用添加函数    
    elif function == 2:#如果用户选择查看
        cat()
    elif function == 3:
        change()
    elif function == 4:
        del_q()
    elif function == 5 and ll == 1:
        print_all()
    elif function == 6:
        break
    else:
        print("输入有误")
    
    
    
    
    
    
    
    
                    


