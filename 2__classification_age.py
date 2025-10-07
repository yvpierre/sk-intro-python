# Pierre YVENOU
# 07/10/2025
# SKEMA BS

## PROGRAMME 2
print("Entrez un age :")
age = input()
if   int(age) <= 12:
    print("Vous êtes ENFANT !")
elif 12 < int(age) < 18:
    print("Vous êtes ADOLESCENT !")
elif 18 <= int(age) < 65:
    print("Vous êtes ADULTE !")
else:
    print("Vous êtes SENIOR !")