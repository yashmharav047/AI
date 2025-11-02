import heapq

# Small Alphabet Graph
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 7), ('E', 3)],
    'C': [('A', 4), ('F', 5)],
    'D': [('B', 7), ('F', 1)],
    'E': [('B', 3), ('F', 8)],
    'F': [('C', 5), ('D', 1), ('E', 8)]
}

# Heuristic (estimated distance to goal F)
heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 2,
    'E': 6,
    'F': 0
}

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

# Run Example
if __name__ == "__main__":
    start, goal = 'A', 'F'
    path, distance = a_star_search(start, goal)
    print("Optimal Path:", " → ".join(path))
    print("Total Distance:", distance, "units")
