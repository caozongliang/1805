a = 0
b = 0

for i in range(101):
    if i%2==0:
        a = a+i
    else:
        b = b +i
print("偶数之和为%d"%a)        
print("奇数之和为%d"%b)    
