list = [[1,3],[5,7],[2,4],[6,8]]
list1 = []
sum = 0
i =0
while i< len(list):
    a = 0

    while a < 2:
        sum1=list[a]
        a+=1
        sum+=sum1
print("和为%d"%sum)        
