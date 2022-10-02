import random


a_luvut = []
b_luvut = []
c_luvut = []
vastaukset = []

for i in range (0, 5):    
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    a_luvut.append(a)
    b_luvut.append(b)
    c_luvut.append(a*b)
    print (f'{a} * {b} = ')
    vastaus = int(input());
    vastaukset.append(vastaus)


oikein = 0

for i in range (0,5):
    if c_luvut[i] == vastaukset[i]:
        print (f'Oikein :) {a_luvut[i]} * {b_luvut[i]} = {c_luvut[i]} ')
        oikein += 1
    else:
        print (f'väärin :( {a_luvut[i]} * {b_luvut[i]} = {c_luvut[i]} ')
        
        
print (f'Sait {oikein} oikein!')
        
    