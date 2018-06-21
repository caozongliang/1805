def sushu(a,b):
    for i in range(a,b):
        flag = 1  
        for j in range(2,i):
            if i%j == 0:
                flag = 0
                break

        if flag == 1:
            print(i)
a = int(input("请输入起始范围"))
b = int(input("请输入终止范围"))
sushu(a,b)        
