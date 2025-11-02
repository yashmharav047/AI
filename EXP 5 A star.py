import heapq

# Simplified Romania Map
graph = {
    'Arad': [('Zerind', 75), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Bucharest': [('Fagaras', 211)]
}

# Heuristic (straight-line distance to Bucharest)
heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Fagaras': 176,
    'Bucharest': 0
}

# A* Search Algorithm
def a_star_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start, [start], 0))
    closed_set = set()

    while open_list:
        f, current, path, g = heapq.heappop(open_list)

        if current == goal:
            return path, g

        if current in closed_set:
            continue
        closed_set.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in closed_set:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(open_list, (f_new, neighbor, path + [neighbor], g_new))

    return None, float('inf')

# Main
if __name__ == "__main__":
    start, goal = 'Arad', 'Bucharest'
    path, distance = a_star_search(start, goal)
    print("Optimal Path:", " → ".join(path))
    print("Total Distance:", distance, "km")
