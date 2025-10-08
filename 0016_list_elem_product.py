# Pierre YVENOU
# 08/10/2025
# SKEMA BS

## PROGRAMME 16
def prod_list(list):
    # 1 et pas 0 pour ne pas faire de produit nul
    res = 1
    for i in list:
        res *= i
    return res

print("Produit des elements de la liste")
print(prod_list([2,1,4]))