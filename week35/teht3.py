import random

a = random.randint(0, 100)
b = random.randint(0, 100)

if a>b:
    print ('a on isompi kuin b')
elif b>a:
    print('b on isompi kuin a')
else:
    print ('yhtäsuuret')