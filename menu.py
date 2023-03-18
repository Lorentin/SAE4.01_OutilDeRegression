import gradient
import ResolutionAnalytique
import indicateurs
import os

def afficherFichier():
    fichiers = os.listdir("fichierTests/")
    for fichier in fichiers:
        print("- " + fichier)


print("------Menu------")
print("1 - Résolution analytique")
print("2 - Descente de gradient")
print("3 - Afficher indicateurs")

while True:
    choix = input("Choisissez : ")
    # gtestion si transformation impossible
    try:
        choix = int(choix)
    except Exception as e:
        choix = 0

    # résolution analytique
    if int(choix) == 1:
        # affichage fichier disponible
        print("------------------------------")
        afficherFichier()
        # choix et lancement algorithme
        while True:
            try:
                fichier = "fichierTests/" + input("Choisissez votre fichier : ") + ".txt"
                ResolutionAnalytique.lancement(fichier)
                break
            except IOError as e:
                print("Erreur choix incorrect")
        break
    # descente de gradient
    elif int(choix) == 2:
        # affichage fichier disponible
        print("------------------------------")
        afficherFichier()
        # choix et lancement algorithme
        while True:
            try :
                fichier = "fichierTests/" + input("Choisissez votre fichier : ") + ".txt"
                gradient.lancement(fichier)
                break
            except IOError as e:
                print("Erreur choix incorrect")
        break
    elif int(choix) == 3:
        # affichage fichier disponible
        print("------------------------------")
        afficherFichier()
        # choix et lancement algorithme
        while True:
            try :
                fichier = "fichierTests/" + input("Choisissez votre fichier : ") + ".txt"
                indicateurs.lancement(fichier)
                break
            except IOError as e:
                print("Erreur choix incorrect")
        break
    else:
        print("Erreur choix incorrect")