def floyd_warshall(graph):
    # Initialize distance and next_node matrices
    nodes = list(graph.keys())
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}
    next_node = {u: {v: None for v in nodes} for u in nodes}

    # Initialize distances based on direct edges
    for u in nodes:
        dist[u][u] = 0
        for v, weight in graph[u]:
            dist[u][v] = weight
            next_node[u][v] = v

    # Floyd-Warshall algorithm
    for k in nodes:
        for i in nodes:
            for j in nodes:
                # Si un chemin plus court est trouvé, 
                # mettre à jour dist[i][j] et définir 
                # next_node[i][j] sur next_node[i][k] 
                # (le prochain nœud sur le chemin de i
                #  à k).
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]
    # Check for negative cycles
    for u in nodes:
        if dist[u][u] < 0:
            raise Exception("Graph contains a negative-weight cycle")

    return dist, next_node

def reconstruct_path(u, v, next_node):
    if next_node[u][v] is None:
        return []
    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path
                  
# Distances les plus courtes :

# A {'A': 0, 'B': 3, 'C': 4, 'D': 5}
# B {'A': 4, 'B': 0, 'C': 1, 'D': 2}
# C {'A': 6, 'B': 9, 'C': 0, 'D': 4}
# D {'A': 2, 'B': 5, 'C': 6, 'D': 0}

# Prochains nœuds sur les chemins les plus courts :

# A {'A': None, 'B': 'B', 'C': 'B', 'D': 'B'}
# B {'A': 'D', 'B': None, 'C': 'C', 'D': 'D'}
# C {'A': 'D', 'B': None, 'C': None, 'D': 'D'}
# D {'A': 'A', 'B': 'A', 'C': 'A', 'D': None}