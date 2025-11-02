# Simplified Romania Map Graph
graph = {
    'Arad': ['Zerind', 'Sibiu'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Bucharest': ['Fagaras']
}

# Depth-Limited DFS
def depth_limited_dfs(graph, start, goal, limit, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    # Goal found
    if start == goal:
        return path
    # Limit reached
    if limit <= 0:
        return None

    visited.add(start)

    # Explore neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = depth_limited_dfs(graph, neighbor, goal, limit - 1, path + [neighbor], visited.copy())
            if result is not None:
                return result
    return None

# Iterative Deepening DFS
def iddfs(graph, start, goal, max_depth=10):
    for depth in range(max_depth):
        print(f"Searching with depth limit = {depth}")
        result = depth_limited_dfs(graph, start, goal, depth)
        if result is not None:
            return result
    return None

# Main
if __name__ == "__main__":
    start_city = "Arad"
    goal_city = "Bucharest"
    path = iddfs(graph, start_city, goal_city)
    if path:
        print(f"\n✅ Path found: {' -> '.join(path)}")
    else:
        print("\n❌ No path found.")
