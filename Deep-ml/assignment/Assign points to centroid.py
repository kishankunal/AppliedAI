# https://www.scaler.com/academy/mentee-dashboard/class/424891/assignment/problems/253597?navref=cl_tt_nv

import math

def assign_to_centroids(points, centroids):
    """
    input:
      points -> list of 2D tuples
      centroids -> list of current centroid tuples

    output:
      list of integers -> index of nearest centroid for each point
    """
    def euclidean_distance(point1, point2):
        return sum((a-b) **2 for a, b in zip(point1, point2))**0.5

    k = len(centroids)
    assignments = []
    for point in points :
        nearest = min(range(k), key = lambda i: euclidean_distance(point, centroids[i]))
        assignments.append(nearest)
 
    return assignments