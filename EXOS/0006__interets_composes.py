# Pierre YVENOU
# 07/10/2025
# SKEMA BS

## PROGRAMME 6
print("Saississez la valeur du capital initial:")
c0 = float(input("Votre choix: "))

print("Saississez la valeur du taux d'intérêt (en %):")
r = float(input("Votre choix: "))
print("Saississez la valeur du nombre d'années:")
n = int(input("Votre choix: "))

# Explication de la formule:
#   capital initial * (1 + taux/100)^nombre d'années
c = c0 * (1 + r/100)**n
print("Le capital après"+str(n)+"années sera de:"+ str(round(c,2))+ "euros.")