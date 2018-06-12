i = 1 
ou = 0
while i < 100:
    if i % 2 == 0:
        ou = ou - i
    else:
        ou = ou + i
    i+=1
print(ou)
