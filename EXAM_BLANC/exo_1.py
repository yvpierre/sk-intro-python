# Pierre YVENOU
# 04/11/2025
# SKEMA BS

def exo1(chaine, mot): 
    # INIT
    liste_finale = []
    splitee = chaine.split("\n")

    for i in splitee:
        print("Ligne actuelle: "+str(i))
        mot_splittes = i.split()
        
        for j in mot_splittes:
            print("Mot dans la ligne: "+str(j))
            if(j == "PEAR"):
                liste_finale.append(i)

    return liste_finale

print(exo1("APPLE PEAR\nPLUM PEACH\nPEAR PLUM", "PEAR"))