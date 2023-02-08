import matplotlib.pyplot as plt
from pandas import DataFrame

from OuvertureFichier import ouvertureFichier


class ResolutionAnalytique:

    def indicateur(dataFrame) -> tuple():
        """
        Calcul des indicateurs de la covariance et de la variance,
        ajoute a la trame de données une colonne xy = (données de la colonne x * données de la colonne de y)
        ajoute a la trame de données une colonne avec les valeurs de la colonne x au carré
            Calcul covariance = moyenne xy - (moyenne x * moyenne Y)
            Calcul variance = moyenne quadratique de x (x^2) - (moyenne de x)^2
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
        :param dataFrame:
        :return:
        """
        covariance = indicateurs[0]
        variance = indicateurs[1]

        # calcul de alpha
        try:
            alpha = covariance / variance
        except ZeroDivisionError:
            print("div zero")

        # calcul de Beta = moyenne y - alpha * moyenne x
        beta = dataFrame['y'].mean() - alpha * dataFrame['x'].mean()

        facteurs = (alpha, beta)

        return facteurs

    def fonction(facteur, dataFrame) -> DataFrame:
        fn = facteur[0] * dataFrame['x'] + facteur[1]
        return fn

    def affichage(dataFrame, fn) -> None:
        """
        Affiche le nuage de point a partir des colonnes x et y de la trame de données
        ainsi que la courbe de de la fonction passée en parametres
        :param fn: fonction y = alpha * colonne de données de x + beta
        """
        dataFrame.plot.scatter(x="x", y="y")
        plt.plot(dataFrame['x'], fn)
        plt.show()

    tab = {'x': [32, 48, 60, 157, 76, 90],
           'y': [69.5, 299, 146, 471.6, 66, 190]
           }

    try:
        jeuxDonnees = ouvertureFichier("test.txt")
        indicateurs = indicateur(jeuxDonnees)
        facteur = facteurFn(indicateurs, jeuxDonnees)
        fonction = fonction(facteur, jeuxDonnees)
        affichage(jeuxDonnees, fonction)
    except Exception as e:
        print(e)
