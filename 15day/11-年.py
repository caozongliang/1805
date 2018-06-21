def year_12(year):
    if (year%4==0 and year%100!=0) or year%400==0:
           print("闰年")
    else:
           print("平年")
a = int(input("请输入年份"))
year_12(a)   

