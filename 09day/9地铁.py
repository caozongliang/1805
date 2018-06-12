f = 0
import random
for i in range(60):
    gl = random.randint(1,33)
#*************    #**********
    if f <=100 or f >400: 
        if gl <= 6:
            hf = 3
        elif 6<gl<=12:
            hf = 4
        elif 12<gl<=22:
            hf = 5
        elif 22<gl<=32:
            hf = 6
        else:
            hf = 7
        f+=hf
#print(f)

    elif 100<f<=150:
        
        if gl <= 6:
            hf = 3*0.8
        elif 6<gl<=12:
            hf = 4*0.8
        elif 12<gl<=22:
            hf = 5*0.8
        elif 22<gl<=32:
            hf = 6*0.8
        else:
            hf = 7*0.8
        f+=hf

        if gl <= 6:
            hf = 3
        elif 6<gl<=12:
            hf = 4
        elif 12<gl<=22:
            hf = 5
        elif 22<gl<=32:
            hf = 6
        else:
            hf = 7
        f+=hf
#print(f)

    elif f >150: 
        if gl <= 6:
            hf = 3
        elif 6<gl<=12:
            hf = 4
        elif 12<gl<=22:
            hf = 5
        elif 22<gl<=32:
            hf = 6
        else:
            hf = 7
        f+=hf
print(f)        
