# Pierre YVENOU
# 07/10/2025
# SKEMA BS

## PROGRAMME 12
print("Jusqu'à quel nombre voulez vous voir la suite de fibonacci ?")
n = input()
a, b = 0, 1
suite = []
while a <= int(n):
    suite.append(a)
    a, b = b, a + b
print("La suite de Fibonacci jusqu'à"+str(n)+"est :"+str(suite))