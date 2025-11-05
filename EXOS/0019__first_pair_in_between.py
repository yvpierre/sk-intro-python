# Pierre YVENOU
# 08/10/2025
# SKEMA BS

## PROGRAMME 19
def nb_above(liste, m):
    sorted = liste
    sorted.sort()
    res = [];
    for i in range(len(sorted)):
        if sorted[i] >= m: res=sorted[i:]; break
    return res;
    
def nb_below(liste, m):
    sorted = liste
    sorted.sort()
    res = [];
    for i in range(len(sorted)):
        if sorted[i] >= m: res=sorted[:i]; break
    return res;

def list_between(liste, a, b):
    sorted = liste
    sorted.sort()
    res = [];
    above = nb_above(liste, a)
    below = nb_below(liste, b)
    res = [value for value in above if value in below]
    return res

def first_pair_elem(liste):
    print([value for value in liste if value%2==0][0])
    
liste1 = list_between([1,4,5,103,2,841,24], 3,25)
first_pair_elem(liste1)