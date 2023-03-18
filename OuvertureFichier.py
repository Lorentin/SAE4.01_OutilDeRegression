import pandas
from pandas import DataFrame


def ouvertureFichier(name) -> DataFrame:
    """
    Ouverture d'un fichier texte et traitement des données pour les passer sous format trame de données avec les colonnes x et Y
    :param name: Nom du fichier a ouvrir
    :return: Renvoie une trame de données avec une colonne x et y
    """

    x = []
    y = []
    # dictionnaire des données
    donnees = {
        'x': x,
        'y': y
    }
    try:
        with open(name) as f:
            lines = f.readlines()

            if not lines:
                raise Exception("Nombre de donnée invalide")
            else:
                for line in lines:
                    # Enleve les sauts de ligne en fin de ligne et sépare les données a l'aide de la tabulation
                    line = line.replace('\n', '')
                    a = line.split("\t")

                    # Vérifie si on a recuperé assez de données sur la ligne sinon on renvoie une Exception
                    if len(a) != 2:
                        raise Exception("Nombre de donnée invalide")

                    # Enleve les espaces restant puis passse la donnée en nombre flottant sinon renvoie une Exception
                    # puis l'ajoute dans une des listes
                    try:
                        x.append(float(a[0].replace("\b", "")))
                        y.append(float(a[1].replace("\b", "")))
                    except ValueError:
                        raise ValueError("Erreur de conversion en float")

        # Création d'une frame de données a partir du dictionnaire de données
        jeuxDonnees = pandas.DataFrame(donnees)

        return jeuxDonnees

    except IOError:
        raise IOError("Fichier introuvable")


