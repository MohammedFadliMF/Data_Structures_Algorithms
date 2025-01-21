# on donne la liste des sommets du graphe: 
# S=[0,1,2,3,4,5,6] 
# et les arrêts de G sous forme de liste de tuples :
# A=[(0,1),(0,2),(1,2),(1,5),(2,3),(2,4),(3,6),(4,6),(5,6)
def MatAdj(S, A):
    n = len(S)  # Nombre de sommets
    M = [[0] * n for _ in range(n)]  # Initialisation de la matrice d'adjacence avec des 0

    for (u, v) in A:
        M[u][v] = 1 
        M[v][u] = 1  

    return M
def degre(s, M):
    return sum(M[s])  

# Un graphe est eulérien s'il possède un cycle eulérien, 
# c'est-à-dire un cycle qui passe par chaque arête 
# exactement une fois. Pour qu'un graphe soit eulérien, 
# il doit satisfaire les conditions suivantes :

# 1- Tous les sommets doivent avoir un degré pair.
# 2- Le graphe doit être connexe (tous les sommets doivent
#  être connectés directement ou indirectement)

# Sommet 1 : degré 3 ,Sommet 6 : degré 3
# Le graphe G n'est pas eulérien, car il contient des
#  sommets de degré impair.

def DFS(graph, start):
    visited = set()  # Ensemble pour stocker les sommets visités
    stack = [start]  # Pile pour gérer les sommets à visiter

    while stack:
        vertex = stack.pop()  # Dépiler un sommet
        if vertex not in visited:
            print(vertex, end=" ")  # Traiter le sommet (ici, on l'affiche)
            visited.add(vertex)  # Marquer le sommet comme visité
            # Empiler les voisins non visités
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

from collections import deque

def BFS(graph, start):
    visited = set()  # Ensemble pour stocker les sommets visités
    queue = deque([start])  # File pour gérer les sommets à visiter

    while queue:
        vertex = queue.popleft()  # Défiler un sommet
        if vertex not in visited:
            print(vertex, end=" ")  # Traiter le sommet (ici, on l'affiche)
            visited.add(vertex)  # Marquer le sommet comme visité
            # Enfiler les voisins non visités
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
# Exemple
graph = {
    0: [1, 2],
    1: [0, 2, 5],
    2: [0, 1, 3, 4],
    3: [2, 6],
    4: [2, 6],
    5: [1, 6],
    6: [3, 4, 5]
}

print("Parcours en profondeur (DFS) :")
DFS(graph, 0)  # Commencer à partir du sommet 0
print("Parcours en largeur (BFS) :")
BFS(graph, 0)  # Commencer à partir du sommet 0