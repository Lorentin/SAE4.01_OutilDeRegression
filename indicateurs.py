from OuvertureFichier import ouvertureFichier

def correlationLineaire(jeuxDonnees) -> float:
    """
    Caclul le coefficient de correlation linéaire à l'aide des colonnes X et Y
    :param jeuxDonnees: trame de données du fichier de données
    :return: renvoie 0.0 si dénominateur == 0 pour éviter division par 0 sinon renvoie le coefficient calculé
    """
    moyenne_x = jeuxDonnees['x'].mean()
    moyenne_y = jeuxDonnees['y'].mean()
    jeuxDonnees['sumXY'] = (jeuxDonnees['x'] - moyenne_x) * (jeuxDonnees['y'] - moyenne_y)
    numerateur = jeuxDonnees['sumXY'].sum()

    jeuxDonnees['sumX'] = (jeuxDonnees['x'] - moyenne_x)**2
    denominateur_x = jeuxDonnees['sumX'].sum()

    jeuxDonnees['sumY'] = (jeuxDonnees['y'] - moyenne_y) ** 2
    denominateur_y = jeuxDonnees['sumY'].sum()

    denominateur = (denominateur_x * denominateur_y) ** 0.5
    if denominateur == 0.0:
        return 0.0
    return round(numerateur / denominateur, 2)

def ecartType(jeuxDonnees, lettre, facteur) -> float:
    """
    Calcul de l'écart-type de la colonne
    :param jeuxDonnees: trame de données du fichier de données
    :param lettre: lettre indiquant la colonne
    :param facteur: facteurs de la variance
    :return: écart-type de la colonne
    """
    taille = jeuxDonnees[lettre].size
    if taille < 2:
        return 0.0
    return round(facteur ** 0.5, 2)


def covariance(dataFrame) -> float:
    """
    Calcul des indicateurs de la covariance,
    ajoute a la trame de données une colonne xy = (données de la colonne x * données de la colonne de y)
        Calcul covariance = moyenne xy - (moyenne x * moyenne Y)
    :param dataFrame: trame de données du fichier de données
    :return: Renvoie un tuple avec la covariance et la variance
    """

    # Ajout de colonne pour les calculs d'indicateurs
    dataFrame['xy'] = (dataFrame['x'] * dataFrame['y'])

    # Calcul covariance = moyenne xy - (moyenne x * moyenne Y)
    covariance = (dataFrame['xy'].mean() - dataFrame['x'].mean() * dataFrame['y'].mean())

    return round(covariance, 2)


def indicateursY(jeuxDonnees):
    """
    Affiche les principaux indicateurs de la colonne Y
    :param jeuxDonnees: trame de données du fichier de données
    """
    jeuxDonnees['y^2'] = jeuxDonnees['y'] * jeuxDonnees['y']
    # Calcul variance = moyenne quadratique de y (y^2) - (moyenne de y)^2
    varianceY = (jeuxDonnees['y^2'].mean() - jeuxDonnees['y'].mean() * jeuxDonnees['y'].mean())

    print("moyenne colonne Y = " + str(round(jeuxDonnees['y'].mean(), 2)))
    print("médianes colonne Y = " + str(round(jeuxDonnees['y'].median(), 2)))
    print("étendue colonne Y = " + str(round(jeuxDonnees['y'].max() - jeuxDonnees['y'].min(), 2)))
    print("variance Y = " + str(round(varianceY, 2)))
    print("écart-type de la colonne Y = " + str(round(ecartType(jeuxDonnees, 'y', varianceY), 2)))


def indicateursX(jeuxDonnees):
    """
    Affiche les principaux indicateurs de la colonne X
    :param jeuxDonnees: trame de données du fichier de données
    """

    jeuxDonnees['x^2'] = jeuxDonnees['x'] * jeuxDonnees['x']
    # Calcul variance = moyenne quadratique de x (x^2) - (moyenne de x)^2
    varianceX = (jeuxDonnees['x^2'].mean() - jeuxDonnees['x'].mean() * jeuxDonnees['x'].mean())

    print("moyenne colonne X = " + str(round(jeuxDonnees['x'].mean(), 2)))
    print("médianes colonne X = " + str(round(jeuxDonnees['x'].median(), 2)))
    print("étendue colonne X = " + str(round(jeuxDonnees['x'].max() - jeuxDonnees['x'].min(), 2)))
    print("variance X = " + str(round(varianceX, 2)))
    print("écart-type colonne X = " + str(round(ecartType(jeuxDonnees, 'y', varianceX), 2)))


def lancement(fichier):
    try:
        jeuxDonnees = ouvertureFichier(fichier)

        # indicateurs sur les colonnes X et Y
        indicateursX(jeuxDonnees)
        indicateursY(jeuxDonnees)

        print("covariance = " + str(round(covariance(jeuxDonnees), 2)))
        print("coefficient de corrélation linéaire = " + str(round(correlationLineaire(jeuxDonnees), 2)))
    except ValueError:
        print("Fichier Illisible merci de relancer avec un autre fichier")
    except Exception:
        print("Fichier Illisible merci de relancer avec un autre fichier")
