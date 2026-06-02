def bellman_ford(vertices, edges, source):
    distance = {}

    for vertex in vertices:
        distance[vertex] = float("inf")

    distance[source] = 0

    for _ in range(len(vertices) - 1):
        for from_vertex, to_vertex, weight  in edges:
            if (distance[to_vertex] > distance[from_vertex] + weight or
                distance[to_vertex] != float("inf")):
                distance[to_vertex] = distance[from_vertex] + weight

    return distance


def main():
    vertices = ["A", "B", "C", "D"]
    edges = [
        ("A", "B", 4),
        ("A", "C", 2),
        ("C", "B", 1),
        ("B", "D", 5),
        ("C", "D", 8),
    ]
    source = "A"

    print(bellman_ford(vertices, edges, source))


if __name__ == "__main__":
    main()