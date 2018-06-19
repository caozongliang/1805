list = [{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]
print(list)
for i in list:#去掉中括号
    #print(i)
    for k,v in i.items():#k等于beijing..shanghai
        #print(k,v)
        for j,l in v.items():
                print(k,j,l)
