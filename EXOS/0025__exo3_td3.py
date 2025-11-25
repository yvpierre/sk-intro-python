# Pierre YVENOU
# 05/11/2025
# SKEMA BS

## EXO 3 TD 3
def lire_fichier(file_name):
    file = open(file_name, "r")
    content = file.read()
    file.close()
    return content

def ecrire_fichier(source, output):
    texte = lire_fichier(source)
    with open(output, "w") as file:
        file.write("Début du nouveau fichier")
        file.write(texte)
        file.write("Fin du nouveau fichier")

ecrire_fichier("exo3.txt", "test.txt")
print(lire_fichier("test.txt"))
