import heapq
def a_star(graphe, start, goal):
    """
    Classic A* Implementation:
    - Uses a priority queue to store (f_score, node).
    - Reconstructs the path after the algorithm completes using the `previous_nodes` dictionary.
    - Suitable for graphs where the path reconstruction is needed after the search.
    """
    distances = {node: float('infinity') for node in graphe}
    distances[start] = 0  # Distance au nœud de départ
    previous_nodes = {node: None for node in graphe}  # Pour retrouver le chemin

    # Initialisation de la file prioritaire des nœuds 
    # à explorer avec (f_score, nœud)
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Sélectionnez le nœud avec le coût le plus bas, nœud à traiter
        current_f_score, current_node = heapq.heappop(priority_queue)
        
        # Si le nœud actuel est l'objectif, nous avons terminé
        if current_node == goal:
            break
        
        # sinon, explorer le nœud courant
        for neighbor in graphe[current_node]:
            g_score = distances[current_node] + distance(current_node, neighbor)
            if g_score < distances[neighbor]:
                distances[neighbor] = g_score
                previous_nodes[neighbor] = current_node
                f_score = g_score + heuristic(neighbor,goal)   # Valeur qui détermine la priorité dans la file H
               
                heapq.heappush(priority_queue, (f_score, neighbor))
    
    return distances[goal], build_path(previous_nodes, start, goal)

def heuristic(x,y):  # fonction heuristique, distance de Manhattan
    return abs(y[0] - x[0]) + abs(y[1] - x[1])

def distance(x, y):
    return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5

def build_path(previous_nodes, start, goal):
    actual = goal
    chemin = [actual]
    while actual != start:
        actual = previous_nodes[actual]
        chemin = [actual] + chemin
    return chemin

def A_star(graph, start, goal, heuristic):
    """
    A* with Path Tracking:
    - Uses a priority queue to store (f_score, g_score, node, path).
    - Tracks the path during the search, eliminating the need for a separate path reconstruction step.
    - Suitable for scenarios where the path is needed immediately during the search.
    """
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))  # (f_score, g_score, node, path)
    closed_set = set() 

    while open_set:
        f_score, g_score, current_node, path = heapq.heappop(open_set)

        if current_node == goal:
            return path  # Shortest path found

        if current_node in closed_set:
            continue
        
        closed_set.add(current_node)

        for neighbor, weight in graph[current_node]:
            if neighbor in closed_set:
                continue
            tentative_g_score = g_score + weight
            tentative_f_score = tentative_g_score + heuristic(neighbor, goal)
            heapq.heappush(open_set, (tentative_f_score, tentative_g_score, neighbor, path + [neighbor]))

    return None  # Path not found