# Pierre YVENOU
# 05/11/2025
# SKEMA BS

## EXO SUPP TD 3
def dict_de_2_lists(liste_cles, liste_valeurs):
    dictio = {}
    for i in range(len(liste_cles)):
        dictio[liste_cles[i]] = liste_valeurs[i]
    return dictio


liste_1 = ['a', 'b','c']
liste_2 = [2,3,1]
res = dict_de_2_lists(liste_1, liste_2)
for e in res:
    print("Item: "+str(e)+" // Valeur: "+str(res[e]))
