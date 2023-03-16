from pandas import DataFrame

from OuvertureFichier import ouvertureFichier

def miseEnForme(dataFrame) -> DataFrame:
    """
    Ajoute les colonnes nécessaire pour les prochains calcul
    :param dataFrame: Trame de données récuperée du fichier
    :return: Trame de données avec les colonnes necessaire pour les prochains calcul
    """
    # Ajout de colonne pour les calculs d'indicateurs
    dataFrame['xy'] = dataFrame['x'] * dataFrame['y']
    dataFrame['x^2'] = dataFrame['x'] ** 2
    dataFrame['y^2'] = dataFrame['y'] ** 2
    dataFrame['x^2'] = dataFrame['x'] ** 2

    return dataFrame

def deriveePartielleA(a, b, sommeXc, sommeX, sommeXY) -> float:
    """
    Calcul du gradient de "a" à partir de sa derivée partiel
    :param a: parametres de la pente
    :param b: ordonnée a l'origine
    :param sommeXc: somme de la colonne des X au carré
    :param sommeX: somme de la colonne des X
    :param sommeXY: somme de la colonne des XY (x * y)
    :return: résultat du calcul de gradient de a
    """
    return 2 * (a * sommeXc + b * sommeX - sommeXY)

def deriveePartielleB(a, b, sommeX, tailleX, sommeY) -> float:
    """
    Calcul du gradient de "b" à partir de sa derivée partiel
    :param a: parametres de la pente
    :param b: ordonnée a l'origine
    :param sommeX: somme de la colonne des X
    :param tailleX : nombre de données dans le jeu de données (correspond a la taille de la colonne des X)
    :param sommeY: somme de la colonne des Y
    :return: résultat du calcul de gradient de b
    """
    return 2 * (a * sommeX + b * tailleX - sommeY)

def cout(a, b , sommeX, sommeXY, sommeYc, sommeXc, sommeY, n) -> float:
    """
    Calcul de l'erreur possible a chaque rapprochement du minimum
    :param a: parametres de la pente
    :param b: ordonnée a l'origine
    :param sommeX: somme de la colonne des X
    :param sommeXY: somme de la colonne des XY (x * y)
    :param sommeYc: somme de la colonne des Y au carré
    :param sommeXc: somme de la colonne des X au carré
    :param sommeY: somme de la colonne des Y
    :param n: nombre de données dans le jeu de données (correspond a la taille de la colonne des X)
    :return: résultat du calcul de cout
    """
    return sommeYc - (2 * a * sommeXY) - (2 * b * sommeY) + (a**2 * sommeXc) + (2 * a * b * sommeX) + n * b**2

def gradient(a, b, pas, dataFrame) -> tuple():
    """
    Cherche le minimum locale d'un modéle
    :param a: parametres de la pente
    :param b: ordonnée a l'origine
    :param pas: definit la direction dans laquelle on se déplace
    :param dataFrame: Trame de données qui servira pour le modele
    :return: renvoie les coordonnées du point correspondant a un minimum locale
    """

    # initialisation pour eviter les calculs redondant
    sommeX = dataFrame['x'].sum()
    sommeXY = dataFrame['xy'].sum()
    sommeY = dataFrame['y'].sum()
    tailleX = dataFrame['x'].size
    sommeYc = dataFrame['y^2'].sum()
    sommeXc = dataFrame['x^2'].sum()

    # initialisation du nombre d'itérations
    iteration = 0

    # Premier calcul de cout avec valeur a et b par défaut
    coutPrecedent = cout(a, b, sommeX, sommeXY, sommeYc, sommeXc, sommeY, tailleX)

    #boucle pour trouver le minimum du modèle
    while True:
        # calcul du cout apres changement des a et b pour savoir si on réduit le pas
        coutSuivant = cout(a, b, sommeX, sommeXY, sommeYc, sommeXc, sommeY, tailleX)
        if coutPrecedent < coutSuivant:
            pas = pas / 100
        coutPrecedent = coutSuivant

        # calcul des gradient de a et b à partir de leurs dérivées partiels
        derivA = deriveePartielleA(a, b, sommeXc, sommeX, sommeXY)
        derivB = deriveePartielleB(a, b, sommeX, tailleX, sommeY)

        # ajustement de notre a et b pour se rapprocher des coordonnées du miminimum de notre modele
        a = a - pas * derivA
        b = b - pas * derivB

        iteration += 1
        # Test pour sortir de la boucle ou non
        # Test si convergence d'un des 2 gradients
        # Ou test si on arrive a limite d'iterations definit
        if abs(derivA) <= 1E-15 or abs(derivB) <= 1E-15 or iteration == 1000000:
            break

    resultat = (a, b)
    return resultat


jeuxDonnees = ouvertureFichier("test.txt")
miseEnForme(jeuxDonnees)
print(gradient(a = 15, b = 15, pas = 100, dataFrame=jeuxDonnees))
