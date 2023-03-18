import gradient
import ResolutionAnalytique
import indicateurs
import os


def afficherFichier():
    fichiers = os.listdir("fichierTests/")
    for fichier in fichiers:
        print("- " + fichier)


def testConversion(choix):
    try:
        return int(choix)
    except Exception as e:
        return 0

def calculSurface(facteurs):
    """
    Calcul de a partir d'une surface et du modéle trouvé
    :param facteurs: a et b permettant le calcul à partir du modele
    :return: estimation d un prix a partir de la surface
    """
    surface = input("Entrez la surface : ")
    try:
        surface = int(surface)
        print(str(facteur[0] * surface + facteur[1]))
    except Exception as e:
        raise e

def dernierChoix(facteur):
    # Dernier choix
    print("------------------------------")
    print("1 - Calculer une estimation du prix")
    print("2 - Quitter")
    while True:
        choix = input("Choisissez : ")
        choix = testConversion(choix)
        if int(choix) == 1:
            while True:
                try:
                    calculSurface(facteur)
                    break
                except Exception:
                    choix = 0
            break
        elif int(choix) == 2:
            break
        print("choix incorrect")


print("------Menu------")
print("1 - Résolution analytique")
print("2 - Descente de gradient")
print("3 - Afficher indicateurs")

while True:
    choix = input("Choisissez : ")
    # gestion si transformation impossible
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
                facteur = ResolutionAnalytique.lancement(fichier)
                dernierChoix(facteur)
                break
            except Exception as e:
                print("Erreur choix incorrect")
        break
    # descente de gradient
    elif int(choix) == 2:
        # affichage fichier disponible
        print("------------------------------")
        afficherFichier()
        # choix et lancement algorithme
        while True:
            try:
                fichier = "fichierTests/" + input("Choisissez votre fichier : ") + ".txt"
                facteur = gradient.lancement(fichier)
                dernierChoix(facteur)
                break
            except Exception as e:
                print("Erreur choix incorrect")
        break
    elif int(choix) == 3:
        # affichage fichier disponible
        print("------------------------------")
        afficherFichier()
        # choix et lancement algorithme
        while True:
            try:
                fichier = "fichierTests/" + input("Choisissez votre fichier : ") + ".txt"
                indicateurs.lancement(fichier)
                break
            except IOError as e:
                print("Erreur choix incorrect")
        break
    else:
        print("Erreur choix incorrect")
