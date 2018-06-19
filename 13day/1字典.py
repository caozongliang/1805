#字典是无序的*********************************************
'''
身份证
姓名：
出生年月：
地址：
名族：


'''
id_card = {"name":"老王","birthday":"1991.12.12","adress":"隔壁","eth":"爱新觉罗","sex":"男"}
print(id_card)
#添加
id_card["age"]=16

id_card.setdefault("height",175)
print(id_card)
#修改
id_card["name"]="老宋"
#查
print(id_card["name"])
print(id_card.get("hahaha"))


#删除
#id_card.pop("name")
id_card.popitem()#随机删除，字典是无序的
print(id_card)
#清空
#id_card.clear
#合并





