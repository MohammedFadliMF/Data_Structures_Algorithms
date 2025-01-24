# ALGORITHME DE DIJKSTRA

# Initialisation :
# Traitement du Nœud Courant :
# Marquage et Sélection du Prochain Nœud :
# Répétition :Répéter les étapes 2 et 3 jusqu'à ce que tous les nœuds soient visités ou que la plus petite distance enregistrée parmi les nœuds non visités soit infinie.

import heapq

def dijkstra(graph, start):
    # Initialisation
    # This line initializes a dictionary called distances
    # Setting the distance to "infinity" ensures that any actual calculated distance will always be smaller. It acts as a starting maximum value.
    distances = {node: float('infinity') for node in graph}
    #  distances = {
    #      'A': 0,
    #      'B': 4,
    #      'C': 2,
    #      'D': 9,
    #      'E': 5
    #  }

    distances[start] = 0  # Distance au nœud de départ

    priority_queue = [(0, start)]  # File de priorité avec (distance, nœud)
    # priority_queue = [(4, 'B'), (2, 'C'), (5, 'E')]

    previous_nodes = {node: None for node in graph}  # Pour retrouver le chemin
     # previous_nodes = {
         #     'A': None,
         #     'B': 'A',
         #     'C': 'A',
         #     'D': 'B',
         #     'E': 'C'
     # }

    while priority_queue:
        # Unpacking the Tuple priority_queue
        # This step retrieves the current node to process in Dijkstra's algorithm
        current_distance, current_node = heapq.heappop(priority_queue)

        # Si la distance courante est déjà plus grande que celle enregistrée, on saute 
        #  continue permet de passer à l'itération suivante de la boucle sans faire d'autres calculs pour ce nœud, évitant ainsi des traitements inutiles
        if current_distance > distances[current_node]:
            continue

        # Exploration des voisins
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Mise à jour de la distance si un chemin plus court est trouvé
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

# Exemple de graphe (A, B, C, D, E avec leurs poids)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    'C': {'E': 3},
    'D': {},
    'E': {'D': 4}
}

# Exécuter l'algorithme depuis le nœud de départ 'A'
distances, previous_nodes = dijkstra(graph, 'A')

# Affichage des résultats
print("Distances les plus courtes depuis 'A' :")
for node, distance in distances.items():
    print(f"Distance vers {node} : {distance}")

print("\nChemins optimaux :")
for node in graph:
    path = []
    current = node
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    print(f"Chemin vers {node} : {' -> '.join(reversed(path))}")

 