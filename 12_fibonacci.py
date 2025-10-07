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
print("La suite de Fibonacci jusqu'à", n, "est :", suite)

git commit -m "exos séance 1"
git branch -M main
git remote add origin https://github.com/yvpierre/sk-intro-python.git
git push -u origin main