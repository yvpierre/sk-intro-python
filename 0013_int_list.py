# Pierre YVENOU
# 07/10/2025
# SKEMA BS

## PROGRAMME 13
print("Saississez le premier entier à ajouter dans la liste (STOP pour arrêter):")
liste = []
val = input()
if(val != 'STOP'):  
    liste.append(int(val))
    while(val != 'STOP'):
        print("Saississez un entier à ajouter dans la liste (STOP pour arrêter):")
        val = input()
        if(val != 'STOP' and val != ''):
            liste.append(int(val))

# On affiche la liste
print("Etat final de la liste")
for i in liste: 
    print(i)
