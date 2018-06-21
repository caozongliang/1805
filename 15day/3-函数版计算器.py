def j(a,b,c):
    if c == "+":
        print("%d+%d=%d"%(a,b,a+b))
    elif c == "-":
        print("%d-%d=%d"%(a,b,a-b))
    elif c == "*":
        print("%d*%d=%d"%(a,b,a*b))
    elif c == "/":
        if b != 0:
            print("%d/%d=%.2f"(a,b,a/b))
        elae:    
            print("输入不合法")

j(1,2,"+")        
j(3,3,"*")
    
    
#***************************************
def j():
    a = int(input("输入数值"))
    b = int(input("输入数值"))
    c = input("输入符号")
    
    if c == "+":
        print("%d+%d=%d"%(a,b,a+b))
    elif c == "-":
        print("%d-%d=%d"%(a,b,a-b))
    elif c == "*":
        print("%d*%d=%d"%(a,b,a*b))
    elif c == "/":
        print("%d/%d=%.2f"(a,b,a/b))
j()
