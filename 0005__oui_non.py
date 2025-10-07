# Pierre YVENOU
# 07/10/2025
# SKEMA BS

## PROGRAMME 5
print("Tapez OUI ou NON (STOP pour arrêter):")
res = input("Votre choix: ").upper()

if(res != "OUI" and res != "NON" and res != "STOP"):
    print("Réponse invalide, rentrez une valeur correcte !")
    res = input("Votre choix: ").upper()
else:
    while res != "STOP":
        if(res == "OUI"):
            print("NON")
            res = input("Votre réponse: ").upper()
        elif(res == "NON"):
            print("OUI")
            res = input("Votre réponse: ").upper()
        elif(res != "OUI" and res != "NON" and res != "STOP"):
            print("Réponse invalide, rentrez une valeur correcte !")
            res = input("Votre choix: ").upper()