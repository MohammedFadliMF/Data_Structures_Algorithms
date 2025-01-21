def hauteur(arbre):
    # Cas de base : si l'arbre est vide, sa hauteur est -1
    if not arbre:
        return -1
    
    # Récursivement, calculer la hauteur des sous-arbres gauche et droit
    hauteur_gauche = hauteur(arbre[1])  # Sous-arbre gauche
    hauteur_droit = hauteur(arbre[2])   # Sous-arbre droit
    
    # La hauteur de l'arbre est 1 + le maximum des hauteurs des sous-arbres
    return 1 + max(hauteur_gauche, hauteur_droit)

def isfeuille(arbre, noeud):
    if not arbre:
        return False
    
    if arbre[0] == noeud:
        return not arbre[1] and not arbre[2]
    
    return isfeuille(arbre[1], noeud) or isfeuille(arbre[2], noeud)

def nbrnoeuds(arbre):
    # Cas de base : si l'arbre est vide, il n'y a pas de nœuds
    if not arbre:
        return 0
    
    # Compter le nœud actuel + les nœuds des sous-arbres gauche et droit
    return 1 + nbrnoeuds(arbre[1]) + nbrnoeuds(arbre[2])

def nbrnoeuds_iteratif(arbre):
    if not arbre:
        return 0
    
    pile = [arbre]
    compteur = 0
    
    while pile:
        noeud = pile.pop()
        compteur += 1
        
        if noeud[1]:  # Ajouter le sous-arbre gauche à la pile
            pile.append(noeud[1])
        if noeud[2]:  # Ajouter le sous-arbre droit à la pile
            pile.append(noeud[2])
    
    return compteur

def max_arbre(arbre):
    # Cas de base : si l'arbre est vide, retourner une valeur très petite
    if not arbre:
        return float('-inf')  # Représente une valeur infiniment petite
    
    # Trouver le maximum entre :
    # 1. La valeur du nœud actuel
    # 2. La valeur maximale du sous-arbre gauche
    # 3. La valeur maximale du sous-arbre droit
    return max(arbre[0], max_arbre(arbre[1]), max_arbre(arbre[2]))

def max_arbre_iteratif(arbre):
    if not arbre:
        return float('-inf')
    
    pile = [arbre]
    max_val = float('-inf')
    
    while pile:
        noeud = pile.pop()
        max_val = max(max_val, noeud[0])  # Mettre à jour la valeur maximale
        
        if noeud[1]:  # Ajouter le sous-arbre gauche à la pile
            pile.append(noeud[1])
        if noeud[2]:  # Ajouter le sous-arbre droit à la pile
            pile.append(noeud[2])
    
    return max_val

# Pré-ordre (Racine → Gauche → Droite)
def dfs_pre_order(arbre):
    if not arbre:  # Si l'arbre est vide
        return []
    valeur, gauche, droite = arbre
    return [valeur] + dfs_pre_order(gauche) + dfs_pre_order(droite)
# In-ordre (Gauche → Racine → Droite)
def dfs_in_order(arbre):
    if not arbre:  # Si l'arbre est vide
        return []
    valeur, gauche, droite = arbre
    return dfs_in_order(gauche) + [valeur] + dfs_in_order(droite)
# Post-ordre (Gauche → Droite → Racine)
def dfs_post_order(arbre):
    if not arbre:  # Si l'arbre est vide
        return []
    valeur, gauche, droite = arbre
    return dfs_post_order(gauche) + dfs_post_order(droite) + [valeur]
# Parcours en largeur (BFS)
from collections import deque
def bfs(arbre):
    if not arbre:  # Si l'arbre est vide
        return []
    resultat = []
    queue = deque([arbre])  # On commence avec la racine
    while queue:
        noeud = queue.popleft()  #On retire le premier nœud de la file
        valeur, gauche, droite = noeud
        resultat.append(valeur)  # On ajoute la valeur du nœud au résultat
        if gauche:  # Si le sous-arbre gauche existe, on l'ajoute à la file
            queue.append(gauche)
        if droite:  # Si le sous-arbre droit existe, on l'ajoute à la file
            queue.append(droite)
    return resultat


# Suppression dans un arbre binaire de recherche (ABR)
def delete_node_binary_search_tree(arbre, valeur):
    if not arbre:
        return arbre
    
    # Recherche du nœud à supprimer
    if valeur < arbre[0]:
        arbre[1] = supprimer(arbre[1], valeur)
    elif valeur > arbre[0]:
        arbre[2] = supprimer(arbre[2], valeur)
    else:
        # Cas 1 : Le nœud est une feuille ou a un seul enfant
        if not arbre[1]:
            return arbre[2]
        elif not arbre[2]:
            return arbre[1]
        
        # Cas 2 : Le nœud a deux enfants
        # Trouver le successeur (le plus petit dans le sous-arbre droit)
        successeur = trouver_min(arbre[2])
        arbre[0] = successeur[0]  # Remplacer la valeur
        arbre[2] = supprimer(arbre[2], successeur[0])  # Supprimer le successeur
    
    return arbre
def trouver_min(arbre):
    while arbre[1]:
        arbre = arbre[1]
    return arbre
# Suppression dans un arbre binaire quelconque(non ordonné)
def delete_node_general_binary_tree(arbre, valeur):
    if not arbre:
        return arbre
    
    # Si le nœud actuel est celui à supprimer
    if arbre[0] == valeur:
        # Cas 1 : Le nœud est une feuille
        if not arbre[1] and not arbre[2]:
            return []
        # Cas 2 : Le nœud a un seul enfant
        elif not arbre[1]:
            return arbre[2]
        elif not arbre[2]:
            return arbre[1]
        # Cas 3 : Le nœud a deux enfants (on remplace par le sous-arbre gauche)
        else:
            return arbre[1]
    
    # Rechercher dans les sous-arbres
    arbre[1] = delete_node_general_binary_tree(arbre[1], valeur)
    arbre[2] = delete_node_general_binary_tree(arbre[2], valeur)
    
    return arbre
def delete_node_general_binary_tree_iterative(arbre, valeur):
    if not arbre:
        return arbre
    
    # Si la racine est le nœud à supprimer
    if arbre[0] == valeur:
        # Cas 1 : Le nœud est une feuille
        if not arbre[1] and not arbre[2]:
            return []
        # Cas 2 : Le nœud a un seul enfant
        elif not arbre[1]:
            return arbre[2]
        elif not arbre[2]:
            return arbre[1]
        # Cas 3 : Le nœud a deux enfants (on remplace par le sous-arbre gauche)
        else:
            return arbre[1]
    
    # Initialisation de la file pour le parcours BFS
    queue = deque()
    queue.append(arbre)
    
    while queue:
        current_node = queue.popleft()
        
        # Vérifier le sous-arbre gauche
        if current_node[1]:
            if current_node[1][0] == valeur:
                # Cas 1 : Le nœud est une feuille
                if not current_node[1][1] and not current_node[1][2]:
                    current_node[1] = []
                # Cas 2 : Le nœud a un seul enfant
                elif not current_node[1][1]:
                    current_node[1] = current_node[1][2]
                elif not current_node[1][2]:
                    current_node[1] = current_node[1][1]
                # Cas 3 : Le nœud a deux enfants (on remplace par le sous-arbre gauche)
                else:
                    current_node[1] = current_node[1][1]
            else:
                queue.append(current_node[1])
        
        # Vérifier le sous-arbre droit
        if current_node[2]:
            if current_node[2][0] == valeur:
                # Cas 1 : Le nœud est une feuille
                if not current_node[2][1] and not current_node[2][2]:
                    current_node[2] = []
                # Cas 2 : Le nœud a un seul enfant
                elif not current_node[2][1]:
                    current_node[2] = current_node[2][2]
                elif not current_node[2][2]:
                    current_node[2] = current_node[2][1]
                # Cas 3 : Le nœud a deux enfants (on remplace par le sous-arbre gauche)
                else:
                    current_node[2] = current_node[2][1]
            else:
                queue.append(current_node[2])
    
    return arbre
# Suppression dans un arbre général
def delete_node_general_tree(arbre, valeur):
    if not arbre:
        return arbre
    
    # Si le nœud actuel est celui à supprimer
    if arbre[0] == valeur:
        return []  # Supprimer le nœud et tous ses enfants
    
    # Rechercher dans les enfants
    arbre[1:] = [delete_node_general_tree(enfant, valeur) for enfant in arbre[1:]]
    
    return arbre


# Trier,à la main ,la liste suivante en appliquant le tri par tas [2,5,3,89,3,23,12,56]
def tri_par_tas(tableau):
    n = len(tableau)
    
    # Construire un tas max
    for i in range(n // 2 - 1, -1, -1):
        entasser(tableau, n, i)
    
    # Extraire les éléments un par un
    for i in range(n - 1, 0, -1):
        tableau[0], tableau[i] = tableau[i], tableau[0]  # Échanger la racine avec le dernier élément
        entasser(tableau, i, 0)  # Réorganiser le tas réduit
def entasser(tableau, n, i):
    plus_grand = i  # Initialiser le plus grand comme racine
    gauche = 2 * i + 1  # Indice de l'enfant gauche
    droite = 2 * i + 2  # Indice de l'enfant droit
    
    # Si l'enfant gauche est plus grand que la racine
    if gauche < n and tableau[gauche] > tableau[plus_grand]:
        plus_grand = gauche
    
    # Si l'enfant droit est plus grand que la racine
    if droite < n and tableau[droite] > tableau[plus_grand]:
        plus_grand = droite
    
    # Si le plus grand n'est pas la racine
    if plus_grand != i:
        tableau[i], tableau[plus_grand] = tableau[plus_grand], tableau[i]  # Échanger
        entasser(tableau, n, plus_grand)  # Réorganiser le sous-arbre affecté
# Définir la fonction d'entée tamiser(arb,noeud,max) 
# qui prend en paramètre une liste <<arb>>, l'indice
# du noeud à tamiser et l'index max à ne pas dépasser
# pendant le parcours de la liste 
def tamiser(arb, noeud, max):
    """
    Tamise le nœud à l'indice `noeud` dans l'arbre `arb` pour maintenir la propriété du tas max.
    :param arb: Liste représentant l'arbre binaire.
    :param noeud: Indice du nœud à tamiser.
    :param max: Indice maximum à ne pas dépasser dans la liste.
    """
    # Supposer que le nœud actuel est le plus grand
    plus_grand = noeud
    # Indices des enfants gauche et droit
    gauche = 2 * noeud + 1
    droite = 2 * noeud + 2

    # Vérifier si l'enfant gauche est plus grand que le nœud actuel
    if gauche < max and arb[gauche] > arb[plus_grand]:
        plus_grand = gauche

    # Vérifier si l'enfant droit est plus grand que le nœud actuel
    if droite < max and arb[droite] > arb[plus_grand]:
        plus_grand = droite

    # Si le plus grand n'est pas le nœud actuel, échanger et tamiser récursivement
    if plus_grand != noeud:
        arb[noeud], arb[plus_grand] = arb[plus_grand], arb[noeud]  # Échanger
        tamiser(arb, plus_grand, max)  # Tamiser récursivement le sous-arbre affecté

# Les arbres binaires généalogiques

# Fonction pour afficher l'arbre avec des branches
def afficher_arbre(arbre, niveau=0, prefixe=""):
    if arbre:
        valeur, gauche, droite = arbre
        # Afficher le sous-arbre droit
        afficher_arbre(droite, niveau + 1, "/")
        # Afficher le nœud courant avec une indentation
        print(" " * (niveau * 4) + prefixe + str(valeur))
        # Afficher le sous-arbre gauche
        afficher_arbre(gauche, niveau + 1, "\\")


# Exemple
arbre = [10, [5, [2, [], []], [7, [], []]], [15, [6, [], []], [20, [], []]]]

afficher_arbre(arbre)

# print("Avant suppression :", arbre)
# arbre = delete_node_binary_search_tree(arbre, 5)
# print("Après suppression :", arbre)

# print("Hauteur de l'arbre :", hauteur(arbre))  # Output: 2

print("DFS Pré-ordre:", dfs_pre_order(arbre))
print("DFS In-ordre:", dfs_in_order(arbre))
print("DFS Post-ordre:", dfs_post_order(arbre))
print("BFS:", bfs(arbre))

# Exemple d'utilisation Suppression dans un arbre général
arbre = ["A", ["B", ["D", [], []], ["E", [], []]], ["C", [], ["F", [], []]]]
print("Avant suppression :", arbre)
arbre = delete_node_general_tree(arbre, "B")
print("Après suppression de B:", arbre)

tableau = [2,5,3,89,3,23,12,56]
tri_par_tas(tableau)
print("Tableau trié :", tableau)

# Exemple tamisage
arb=[10, 5, 15, 2, 7, 12]
print(arb)
tamiser(arb, 1, 5)
print(arb)