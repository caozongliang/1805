import random
all_money = 0 #消费总钱数
km = 100 #设定固定公里数，（用于检验是否正确）
for i in range(1,31):#每月30天
    for j in range(1,3):#没天两次
        #km = random.randint(1,100)#随机公里数
        if km < 6:#小于6公里
            price = 3#单价
        elif km >6 and km <= 12:
            price = 4
        elif km > 12 and km <= 22:
            price = 5
        elif km > 22 and km <= 32:
            price = 6
        elif km > 32:
            price = int((km-32)/20)+1+6
            #print(price)
        if all_money >= 100 and all_money <=150:
            price = price*0.8
            #print(price)
            #if all_money >150 and all_money<400:

        elif all_money >150 and all_money <= 400:
                price = price*0.5
            #print(price)#验证

        all_money+=price
print("%.2f"%all_money)        
