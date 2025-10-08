# Pierre YVENOU
# 08/10/2025
# SKEMA BS

## PROGRAMME 14
print("Sassissez 'm': ")
m = float(input())

print("Saississez une valeur décimale (STOP pour arrêter): ")
liste = []
val = input()
if(val != 'STOP'):  
    liste.append(float(val))
    while(val != 'STOP'):
        print("Saississez un valeurs décimales à ajouter dans la liste (STOP pour arrêter):")
        val = input()
        if(val != 'STOP' and val != ''):
            liste.append(float(val))

print("m : "+str(m))
print("liste:", liste)

sorted = liste
sorted.sort()
res = 0;
for i in sorted:
    if i >= m: res=i; break
print("Valeur dans la liste qui est la plus proche de m("+str(m)+"): "+str(res))