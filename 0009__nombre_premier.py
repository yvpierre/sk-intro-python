# Pierre YVENOU
# 07/10/2025
# SKEMA BS

## PROGRAMME 9
print("Entrez un nombre pour vérifier s'il est premier :")
n = input()
is_prime = True
if int(n) <= 1:
    is_prime = False
else:
    for i in range(2, int(n)):
        if int(n) % i == 0:
            is_prime = False
            break
if is_prime:
    print(n, "est un nombre premier.")
else:
    print(n, "n'est pas un nombre premier.")
