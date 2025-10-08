# Pierre YVENOU
# 07/10/2025
# SKEMA BS

import time
from time import sleep

## PROGRAMME 3
print("Combien de 'Hello World' ? :")
nb = input()
if(int(nb) > 50):
    print("Trop grand !")
else:
    for i in range(int(nb)):
        print("Hello World !")
        sleep(0.2)