


def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]],
                       max_iterations: int) -> list[tuple[float, ...]]:

    def euclidean_distance(p1, p2):
        return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5

    def assign_cluster(points, centeroids):
        clusters = [[] for _ in range(k)]
        for point in points:
            nearest = min(range(k), key=lambda i: euclidean_distance(point, centeroids[i]))
            clusters[nearest].append(point)
        return clusters

    def compute_centroids(clusters):
        new_centroids = []
        for cluster in clusters:
            dims = len(cluster[0])
            centeroid = tuple(sum(p[d] for p in cluster)/len(cluster) for d in range(dims))
            new_centroids.append(centeroid)
        return new_centroids


    centroids = initial_centroids

    for _ in range(max_iterations):
        clusters = assign_cluster(points, initial_centroids)
        new_centroids = compute_centroids(clusters)
        if new_centroids == initial_centroids:
            break
        centroids = new_centroids

    return [tuple(round(c, 4 ) for c in centroid) for centroid in centroids]