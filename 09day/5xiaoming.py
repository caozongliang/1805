i = 0
while i < 31:
    import random
    t = 0
    while t < 2:
        gl = random.randint(1,33)
        if gl <= 6:
            money = gl*3
        elif 6 < gl <=12:
            money = gl*4
        elif 12 < gl <= 22:
            money = gl*5
        elif 22 < gl <= 32:
            money = gl*6
        else:
            money = gl*6+1
        print("%d"%money)    
        t+=1
    i+=1        
                    






    i+=1
