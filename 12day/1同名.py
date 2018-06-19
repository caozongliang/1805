
name = input("请输入要修改的名字")

list = ['laowang','laoli','laozhao','laowang']
'''
for position,i in enumerate(list):
    if name == i:
        print(position,i)
'''

count = 0
for i in list:
    if name == i:
        print("找到了索引是%d"%count)
    count+=1    
