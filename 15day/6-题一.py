a = [31,29,31,30,31,30,31,31,30,31,30,31]
b = [31,28,31,30,31,30,31,31,30,31,30,31]
def time(year,month,day):
    if (year%4==0 and year%100!=0) or year%400==0:
        xh(a)
    else:
        xh(b)        

def xh(x):        
    c = 0
    sum = 0
    for i in (x):
        c+=1
        sum+=i
        if month==1:
            print("这是今年的第%d天"%day)
            break
        else:
            
            if month == c+1:
            
                print("这是今年的第%d天"%(sum+day))
                break
            #elif month > c:
                #print(" ")    


year = int(input("输入年份"))
month = int(input("输入月份"))
day = int(input("输入几号"))
time(year,month,day)
