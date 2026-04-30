# https://www.scaler.com/academy/mentee-dashboard/class/424891/homework/problems/253588?navref=cl_tt_lst_nm

import math


def k_means_clustering(points, k, initial_centroids, max_iterations):
    def euclidean_distance(point1, point2):
        return sum((a - b) ** 2 for a, b in zip(point1, point2)) ** 0.5

    def assign_cluster(points, centeriod):
        cluster = [[] for _ in range(k)]
        for point in points:
            nearest = min(range(k), key=lambda i: euclidean_distance(point, centeriod[i]))
            cluster[nearest].append(point)
        return cluster

    def updateCenteroids(clusters):
        centeroids = []
        for cluster in clusters:
            dims = len(cluster[0])
            new_centeroids = tuple(sum(p[d] for p in cluster) / len(cluster) for d in range(dims))
            centeroids.append(new_centeroids)
        return centeroids

    centroids = initial_centroids

    for _ in range(max_iterations):
        cluster = assign_cluster(points, centroids)
        new_centroids = updateCenteroids(cluster)
        if new_centroids == centroids:
            break

        centroids = new_centroids

    return [tuple(round(c, 4) for c in centroid) for centroid in centroids]
