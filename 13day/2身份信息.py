'''
card = {"name":"老王","sex":"男","birthday":"1999.2.21","address":"隔壁"}
for i in card:
    print("%s:%s"%(i,card[i]))

print(card)
print(type(card))
#增
card["height"]=175
print(card)
card.setdefault("weight",110)
print(card)
#查
print(card["name"])
print(card["birthday"])#key不存在就报错
print(card.get("lalal"))#key不存在返回  None
#删
card.pop("address")
print(card)
card.popitem()
print(card)
#清空
card.clear()
print(card)
#修改
card["address"]="无处不在"
#print(card)

card.setdefault("weight,110")
print(card["came"])
print(card["cirthday"])
print(card.get("lalala")
'''

 #合并
card = {"name":"老王","sex":"男","birthday":"1999.2.21","address":"隔壁"}
d = {"name":"老宋","11":"aa","22":"bb","eth":"满族"}
card.update(d)#如果key存在，则会覆盖掉
print(card)
'''
for i in card:
    #print("%s:%s"%(i,card[i]))
#for循环/遍历
for k,v in card.items():
    #print(k,v)
#
for i in card.items():
    #print(i)
    for j in i:
        #print(j)






