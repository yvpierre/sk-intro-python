# Pierre YVENOU
# 05/11/2025
# SKEMA BS

## -------- FONCTIONS REUTILISABLES --------
def get_diviseurs(val):
    liste_diviseurs = []
    for i in range(1, val + 1):
        if val % i == 0:
            liste_diviseurs.append(i)
    return liste_diviseurs

def get_nb_premier(n):
    is_prime = True
    if int(n) <= 1:
        is_prime = False
    else:
        for i in range(2, int(n)):
            if int(n) % i == 0:
                is_prime = False
                break
    return is_prime

## -------- EXERCICE 1 --------
def exo1(chaine): 
    tableau_mots = chaine.split()
    res = {}
    for elem in tableau_mots: 
        res[elem] = tableau_mots.count(elem)

    return res;

print("----- EXO 1 -----")
print(exo1("AA AA AA B CC AA B CC CC"))
print("-----------------")


## -------- EXERCICE 2 -------- 
def exo2(liste):
    return [i for i in liste if len(get_diviseurs(i)) == 4]

print("----- EXO 2 -----")
print(exo2([4,12,9,8,6,7,11,12,5,16,7,10,21]))
print("-----------------")

## -------- EXERCICE 4 -------- 
def exo4(dictio_entree):
    return [[i,dictio_entree[i]] for i in dictio_entree if i%2==0 and get_nb_premier(dictio_entree[i])]


print("----- EXO 4 -----")
print(exo4({1:3, 2:5, 7:9, 8:13, 3:11}))
print("-----------------")
