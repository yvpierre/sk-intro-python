# Pierre YVENOU
# 08/10/2025
# SKEMA BS

## PROGRAMME 17
def nb_above(liste, m):
    sorted = liste
    sorted.sort()
    res = [];
    for i in range(len(sorted)):
        if sorted[i] >= m: res=sorted[i:]; break
    print("Valeur dans la liste qui sont supérieures à m("+str(m)+"): "+str(res))

nb_above([2,1,5231,2,92,4,102,5], 6)