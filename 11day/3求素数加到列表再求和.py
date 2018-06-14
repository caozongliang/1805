idh = 0
list = []
for i in range(100,201):
    su = 0
    for j in range(2,i):
        if i%j == 0:
            su = 1
            break
    if su == 0:
        idh+=i
    list.append(i)
print(list)
print("素数的和为%d"%idh)




