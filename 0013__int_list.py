# Pierre YVENOU
# 08/10/2025
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


# On affiche la liste triée
print("Liste triée")
sorted = liste 
sorted.sort()
print(sorted)

# Un entier sur deux 
print("On affiche un element sur deux")
for i in range(len(sorted)):
    if i%2 == 0: print(sorted[i])

# La liste originale inversée
print("on affiche la liste originale à l'envers")
reversed = liste
reversed.reverse()
print(reversed)