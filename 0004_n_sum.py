# Pierre YVENOU
# 07/10/2025
# SKEMA BS

import time
from time import sleep

## PROGRAMME 4
print("Choississez n:")
n = input()
sum = 0;
if(int(n) > 50):
    print("Trop grand !")
else:
    for i in range(int(n)):
        sum += i
        print("On ajoute "+str(i)+", somme =",str(sum))
        sleep(0.2)
print("Total:", sum)