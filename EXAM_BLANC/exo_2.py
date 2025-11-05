# Pierre YVENOU
# 04/11/2025
# SKEMA BS

def get_diviseurs(val):
    liste_diviseurs = []
    for i in range(1, val + 1):
        if val % i == 0:
            liste_diviseurs.append(i)
    return liste_diviseurs

def exo2(liste):
    dictio = {}
    for i in liste:
        produit = get_diviseurs(i)
        print("Produit: "+str(i)+" // Dviseurs: "+str(produit))
        res=1
        for p in produit:
            if p != i or i==1:
                res*=p
        dictio[i] = res

    return dictio;

print(exo2([1,2,6,7,4,9,12]))
