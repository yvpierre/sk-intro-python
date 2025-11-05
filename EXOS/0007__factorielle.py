# Pierre YVENOU
# 07/10/2025
# SKEMA BS

## PROGRAMME 7
print("Entrez un nombre pour calculer sa factorielle :")
n = input()
fact = 1
if(int(n) < 0):
    print("La factorielle n'est pas définie pour les nombres négatifs !")
elif(int(n) == 0):
    print("La factorielle de 0 est 1 !")
else:
    for i in range(1, int(n)+1):
        fact = fact * i
    print("La factorielle de"+str(n)+"est"+str(fact))
