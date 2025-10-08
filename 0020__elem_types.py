# Pierre YVENOU
# 08/10/2025
# SKEMA BS

## PROGRAMME 20
def elem_types(list):
    return [[value, type(value).__name__] for value in list]

print(elem_types(["a",'b',13,19.231,[1,2,3]]))