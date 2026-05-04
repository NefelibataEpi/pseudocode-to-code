
def count_components(graph):
    visited = set()
    count = 0

    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, visited)
            count += 1
    
    return count

def dfs(graph, node, visited):
    visited.add(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    "A": ["B"],
    "B": ["A"],
    "C": ["D"],
    "D": ["C"],
    "E": []
}

print(count_components(graph))