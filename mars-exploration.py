import numpy as np
# I.A.2 Calcul des distances
def calculer_distances(Pi: np.ndarray) -> list:
    """
    Calcule la matrice des distances entre les points d'intérêt et la position du robot.

    Paramètres :
    - Pi : tableau numpy de forme (n, 2) contenant les coordonnées des n points d'intérêt.

    Retour :
    - Une liste de listes (matrice) de taille (n + 1) x (n + 1) contenant les distances entre les points.
      L'indice n représente la position du robot.
    """
    # Récupérer la position actuelle du robot
    x_robot, y_robot = position_robot()
    
    # Nombre de points d'intérêt
    n = len(Pi)
    
    # Créer une matrice de distances de taille (n + 1) x (n + 1) avec des listes Python
    distances = [[0.0] * (n + 1) for _ in range(n + 1)]
    
    # Remplir la matrice avec les distances entre les points d'intérêt
    for i in range(n):
        x1, y1 = Pi[i]
        for j in range(n):
            x2, y2 = Pi[j]
            distances[i][j] = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Remplir la dernière ligne et la dernière colonne (distances entre le robot et les points d'intérêt)
    for i in range(n):
        x, y = Pi[i]
        distance_robot = np.sqrt((x - x_robot)**2 + (y - y_robot)**2)
        distances[i][n] = distance_robot
        distances[n][i] = distance_robot
    
    return distances
# Planification d'une exploration :premiere approche
# A.1 Longueur d'un chemin 
def longueur_chemin(chemin: list, d: np.ndarray) -> float:
    """
    Calcule la distance totale que le robot doit parcourir pour suivre un chemin donné.

    Paramètres :
    - chemin : Liste des indices des points d'intérêt dans l'ordre de parcours.
    - d : Matrice des distances entre les points d'intérêt (y compris la position du robot).

    Retour :
    - La distance totale du chemin.
    """
    # Initialisation de la distance totale
    distance_totale = 0.0
    
    # Position actuelle du robot (dernière ligne/colonne de la matrice d)
    position_actuelle = len(d) - 1
    
    # Parcourir le chemin et accumuler les distances
    for point in chemin:
        distance_totale += d[position_actuelle][point]
        position_actuelle = point
    
    return distance_totale
# A.1 Normalisation  d'un chemin 
def normaliser_chemin(chemin: list, n: int) -> list:
    """
    Normalise un chemin en supprimant les doublons et les valeurs invalides, puis en ajoutant les éléments manquants.

    Paramètres :
    - chemin : Liste d'entiers représentant le chemin à normaliser.
    - n : Entier représentant la limite supérieure (exclue) pour les valeurs valides.

    Retour :
    - Une liste correspondant à un chemin valide, contenant une seule fois tous les entiers entre 0 et n-1.
    """
    # Étape 1 : Supprimer les doublons et les valeurs >= n, en conservant l'ordre relatif
    chemin_filtre = []
    visited = set()  # Pour garder une trace des éléments déjà vus
    for element in chemin:
        if element < n and element not in visited:
            chemin_filtre.append(element)
            visited.add(element)
    
    # Étape 2 : Ajouter les éléments manquants en ordre croissant
    elements_manquants = list(set(range(n)) - visited)
    elements_manquants = tri_selection(elements_manquants)  # Utilisation du tri par sélection
    chemin_normalise = chemin_filtre + elements_manquants
    
    return chemin_normalise
def tri_selection(liste):
    """
    Trie une liste en utilisant l'algorithme de tri par sélection.
    
    Paramètres :
    - liste : Liste à trier.
    
    Retour :
    - Liste triée.
    """
    for i in range(len(liste)):
        # Trouver l'indice du minimum dans la sous-liste non triée
        indice_min = i
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[indice_min]:
                indice_min = j
        
        # Échanger l'élément courant avec le minimum trouvé
        liste[i], liste[indice_min] = liste[indice_min], liste[i]
    
    return liste


