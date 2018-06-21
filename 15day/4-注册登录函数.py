list = []
def zhuce(a,b):
    zi = {}
    if len(a) != 11 or  a.startswith("1") == False or len(b) <=6 or b != bb:
        print("输入有误")
    else:
        import random
        yzm = random.randint(1000,9999)
        print("验证码为:%d"%yzm)
        c = int(input("输入验证码:"))
        if c == yzm:
            print("注册成功")
            zi['account']=a
            zi['password']=b
            list.append(zi)
        else:
            print("注册失败")
a = input("注册账号(手机号)")
b = input("设置密码(大于六位)")
bb = input("再次输入密码")
zhuce(a,b)        
def login(acc,pwd):
    for i in list:
        if acc == i['account'] and pwd == i['password']:
            print('登录成功')
        else:
            print("登录失败")
if list:
    print("请登录:".center(10,' '))        
    acc = input("输入账号")
    pwd = input("输入密码")
    login(acc,pwd)
