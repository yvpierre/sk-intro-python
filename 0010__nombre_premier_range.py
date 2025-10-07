# Pierre YVENOU
# 07/10/2025
# SKEMA BS

## PROGRAMME 10
print("Sélectionnez la première borne de l'intervalle :")
n = input()
print("Sélectionnez la deuxième borne de l'intervalle :")
m = input()
for num in range(int(n), int(m)+1):
    is_prime = True
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        print(num, "est un nombre premier.")
    else:
        print(num, "n'est pas un nombre premier.")
