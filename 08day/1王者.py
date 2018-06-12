
i = 0
while i < 3:
        
    a = input("请输入账号")
    b = input("请输入密码")
    if a == "czl" and b == "123456":
        print("登录成功")
        c = int(input("请选择英雄范围0:ADC 1:肉 3:法师"))
        if c == 0:
            print("鲁班")
            break
        elif c == 1:
            print("程咬金")
            break
        elif c == 3:
            print("王昭君")
            break
        else:
            print("没有")
            break
    else:
        
        print("输入错误，请重新输入")
    
    i+=1
