# Pierre YVENOU
# 05/11/2025
# SKEMA BS

## EXO 1 TD 3
def saisir_actifs():
    dict_actifs = {}
    actif_nom = input("Saississez le nom du premier actif: ")
    if actif_nom != "STOP":
        actif_rendement = input("Saississez le rendement  du premier actif: ")
        dict_actifs[actif_nom] = float(actif_rendement)

    while (actif_nom != "STOP"):
        actif_nom = input("Saississez le nom de l'actif: ")
        if actif_nom != "STOP":
            actif_rendement = input ("Saississez le rendement de l'actif: ")
            dict_actifs[actif_nom] = float(actif_rendement)

    return dict_actifs;


temp = {
    'a': 100.2,
    'b': 3.0,
    'c': 39.1
}

def plus_gros_actif(dictio_actifs):
    maxVal = max(list(dictio_actifs.values()))  
    return [[elem, dictio_actifs[f"{elem}"]] for elem in dictio_actifs if dictio_actifs[f"{elem}"] == maxVal]

print("Plus gros actif: "+plus_gros_actif(temp)[0][0]+" // Valeur du plus gros actif: "+str(plus_gros_actif(temp)[0][1]))