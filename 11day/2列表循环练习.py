a = []
for i in range(1,101,2):
    
    a.append(i)
#print(a)
a.pop()
#print("删除最后一个",a)
a.pop(0)#删除索引上的值
print(a)
a.remove(3)#删除指定值
print(a)
del a[0]#索引
print(a)#系统提供删除方法
#number = a[18]
#print(number,'laowang')



