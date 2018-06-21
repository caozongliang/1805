def print_sum(num):
        
    a = 0
    for i in range(num):
        a+=i
    print(a)
    

print_sum(6)    



#***************************************


def print_sum():
    num = int(input("输入求和范围"))    
    a = 0
    for i in range(num+1):
        a+=i
    print("和为%d"%a)
    

print_sum()    
