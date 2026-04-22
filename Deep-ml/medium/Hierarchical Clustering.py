import numpy as np

def agglomerative_clustering(X: list, n_clusters: int, linkage: str = 'single') -> list:
    n_samples = len(X)
    if n_samples <= n_clusters:
        return list(range(n_samples))

    # Convert to numpy for faster distance calculations on M5 Pro hardware
    data = np.array(X)

    # Precompute pairwise Euclidean distance matrix
    # dist_matrix[i][j] is the distance between point i and point j
    dist_matrix = np.sqrt(((data[:, np.newaxis] - data[np.newaxis, :]) ** 2).sum(axis=2))

    # Initialize clusters: each point is its own cluster
    # Using a dictionary to map cluster_index -> list of sample_indices
    clusters = {i: [i] for i in range(n_samples)}

    while len(clusters) > n_clusters:
        min_dist = float('inf')
        to_merge = (None, None)

        # Sorted keys ensure we respect the "smallest index" requirement
        cluster_indices = sorted(clusters.keys())

        # Step 1: Find the closest pair of clusters
        for i in range(len(cluster_indices)):
            for j in range(i + 1, len(cluster_indices)):
                idx1, idx2 = cluster_indices[i], cluster_indices[j]

                # Calculate inter-cluster distance based on linkage
                points1 = clusters[idx1]
                points2 = clusters[idx2]

                # Subset the precomputed distances for these two clusters
                pairwise_dists = dist_matrix[np.ix_(points1, points2)]

                if linkage == 'single':
                    current_dist = np.min(pairwise_dists)
                elif linkage == 'complete':
                    current_dist = np.max(pairwise_dists)
                elif linkage == 'average':
                    current_dist = np.mean(pairwise_dists)

                # Tie-breaking logic: 
                # 1. Smaller distance 
                # 2. Smaller idx1 (first cluster)
                # 3. Smaller idx2 (second cluster)
                if current_dist < min_dist:
                    min_dist = current_dist
                    to_merge = (idx1, idx2)
                elif current_dist == min_dist:
                    if to_merge == (None, None) or idx1 < to_merge[0] or (idx1 == to_merge[0] and idx2 < to_merge[1]):
                        to_merge = (idx1, idx2)

        # Step 2: Merge clusters
        # Requirement: "Always merge into the cluster with the smaller index"
        c1, c2 = to_merge
        clusters[c1].extend(clusters[c2])
        del clusters[c2]

    # Step 3: Assign final labels based on sorted order of remaining indices
    final_labels = [0] * n_samples
    for label, cluster_idx in enumerate(sorted(clusters.keys())):
        for sample_idx in clusters[cluster_idx]:
            final_labels[sample_idx] = label

    return final_labels