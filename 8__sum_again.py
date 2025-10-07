# Pierre YVENOU
# 07/10/2025
# SKEMA BS

## PROGRAMME 8
print("Entrez un nombre pour calculer la somme de tous les entiers jusqu'à ce nombre :")
n = input()
somme = 0
if(int(n) < 0):
    print("La somme n'est pas définie pour les nombres négatifs !")
elif(int(n) == 0):
    print("La somme de 0 est 0 !")
else:
    for i in range(1, int(n)+1):
        somme += i
    print("La somme de tous les entiers jusqu'à",n,"est",somme)
