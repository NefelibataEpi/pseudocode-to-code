from init_distance_matrix import init_distance_matrix

def floyd_warshall(n, edges):
    dist = init_distance_matrix(n, edges)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist


def main():
    n = 4
    edges = [
        (0, 1, 3),
        (0, 2, 8),
        (1, 2, 2),
        (2, 3, 1)
    ]
    print(floyd_warshall(n, edges))


if __name__ == "__main__":
    main()