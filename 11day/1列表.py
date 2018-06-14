c = ['xingkai','lishuang','laowang']

for i in c:
    print(i)

# add data
#remove data
#change data
#find data
c.append('sunwukong')
print(c)

c.insert(0,'tangseng')
print(c)
c.extend('zhubajie')
print(c)

d = ['laosong']
c.extend(d)
print(c)
c.append(d)
print(c)
