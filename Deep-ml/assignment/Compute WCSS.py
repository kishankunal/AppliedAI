# https://www.scaler.com/academy/mentee-dashboard/class/424891/assignment/problems/253594?navref=cl_tt_nv

def compute_wcss(points, clusters):
    """
    input:
      points -> list of 2D tuples
      clusters -> list of lists, where each sublist contains indices of points in that cluster

    output:
      float -> total WCSS, rounded to 2 decimal places
    """
    def euclidean_squared_distance(point1, point2):
        return sum((a-b) ** 2 for a, b in zip(point1, point2))

    total_wcss = 0

    for cluster in clusters:
        if not cluster:
            continue

        cluster_points = [points[i] for i in cluster]

        dims = len(cluster_points[0])

        centeroid  = tuple(sum(p[d] for p in cluster_points) / len(cluster_points) for d in range(dims))

        for point in cluster_points:
            total_wcss += euclidean_squared_distance(point, centeroid)


    return round(total_wcss, 2)