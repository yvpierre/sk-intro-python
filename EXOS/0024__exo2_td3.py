# Pierre YVENOU
# 05/11/2025
# SKEMA BS

## EXO 2 TD 3
def prod_list(list):
    # 1 et pas 0 pour ne pas faire de produit nul
    res = 1
    for i in list:
        res *= i
    return res

print("Produit des elements de la liste")
print(prod_list([2,1,4,10,412]))

