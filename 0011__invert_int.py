# Pierre YVENOU
# 07/10/2025
# SKEMA BS

## PROGRAMME 11
print("Choississez un nombre à inverser:")
choix = input()
inverser = ""
# range(start, stop, step) avec step négatif pour aller à l'envers
for i in range(len(choix)-1, -1, -1):
    inverser += choix[i]
print("Le nombre inversé est:", inverser)