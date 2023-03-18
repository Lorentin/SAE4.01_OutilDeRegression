from typing import Any

import matplotlib.pyplot as plt

from OuvertureFichier import ouvertureFichier



def indicateur(dataFrame) -> tuple():
    """
    Calcul des indicateurs de la covariance et de la variance,
    ajoute a la trame de données une colonne xy = (données de la colonne x * données de la colonne de y)
    ajoute a la trame de données une colonne avec les valeurs de la colonne x au carré
        Calcul covariance = moyenne xy - (moyenne x * moyenne Y)
        Calcul variance = moyenne quadratique de x (x^2) - (moyenne de x)^2
    :param dataFrame: trame de données du fichier de données
    :return: Renvoie un tuple avec la covariance et la variance
    """

    # Ajout de colonne pour les calculs d'indicateurs
    dataFrame['xy'] = (dataFrame['x'] * dataFrame['y'])
    dataFrame['x^2'] = dataFrame['x'] * dataFrame['x']

    # Calcul covariance = moyenne xy - (moyenne x * moyenne Y)
    covariance = (dataFrame['xy'].mean() - dataFrame['x'].mean() * dataFrame['y'].mean())

    # Calcul variance = moyenne quadratique de x (x^2) - (moyenne de x)^2
    variance = (dataFrame['x^2'].mean() - dataFrame['x'].mean() * dataFrame['x'].mean())

    facteurs = (covariance, variance)

    return facteurs

def facteurFn(indicateurs, dataFrame) -> tuple():
    """
    Calcul des facteurs composant la fonction pour trouver y
        Calcul de alpha = covariance / variance
        Calcul de Beta = moyenne des y - alpha * moyenne des x
    :param dataFrame: Trame de données representant les données du fichier
    :param indicateurs: tuple contenant les indicateurs de la variance et la covariance
    :return: un tuple contenant les facteurs alpha et beta pour créer le model
    """
    covariance = indicateurs[0]
    variance = indicateurs[1]

    # calcul de alpha
    try:
        alpha = covariance / variance
    except ZeroDivisionError:
        print("div zero")

    # calcul de Beta = moyenne des y - alpha * moyenne des x
    beta = dataFrame['y'].mean() - alpha * dataFrame['x'].mean()

    facteurs = (alpha, beta)

    return facteurs

def fonction(facteur, dataFrame) -> tuple[Any, Any]:
    """
    Applique la fonction sur toutes les valeurs de x
    :param dataFrame: Trame de données initial
    :param facteur: tuple contenant alpha et beta
    :return: deux points calulés a partir du modèle
    """

    # Affiche le model trouvée pour calculer les données
    print("------------ Résultat ------------")
    print("y = " + str(round(facteur[0], 2)) + " * x + " + str(round(facteur[1], 2)))

    # Trouve le x le plus petit et le x le plus grand
    # pour trouver "le premier point et le dernier" pour tracer la courbe
    minPoint = dataFrame['x'].min()
    maxPoint = dataFrame['x'].max()

    # Calcul y pour le minimum et le maximum
    dernierY = facteur[0] * minPoint + facteur[1]
    premierY = facteur[0] * maxPoint + facteur[1]
    points = ([dernierY, premierY],[minPoint, maxPoint])

    return points

def affichage(dataFrame, points) -> None:
    """
    Affiche le nuage de point à partir des colonnes x et y de la trame de données
    ainsi que la courbe de la fonction passée en parametres
    :param fn: fonction y = alpha * colonne de données de x + beta
    :param dataFrame : trame de données des données du fichier
    """
    dataFrame.plot.scatter(x="x", y="y")
    plt.plot(points[1], points[0], color="red")
    plt.title('Résolution analytique')
    plt.show()

def lancement(fichier):
    # Lancement de la Résolution par méthode Analytique
    try:
        jeuxDonnees = ouvertureFichier(fichier)
        indicateurs = indicateur(jeuxDonnees)
        facteur = facteurFn(indicateurs, jeuxDonnees)
        fonc = fonction(facteur, jeuxDonnees)
        affichage(jeuxDonnees, fonc)
        return facteur
    except Exception:
        raise Exception("Fichier Illisible merci de relancer avec un autre fichier")