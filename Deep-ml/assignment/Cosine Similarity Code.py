# https://www.scaler.com/academy/mentee-dashboard/class/399309/assignment/problems/26460?navref=cl_tt_nv

import numpy as np
from numpy.linalg import norm


def cosineSimilarity(A, B):
    A_np = np.array(A)
    B_np = np.array(B)

    dot_product = np.dot(A_np, B_np)
    norm_A = norm(A_np)
    norm_B = norm(B_np)

    cosSim = 0

    # Check if either norm is zero to avoid division by zero
    if norm_A != 0 and norm_B != 0:
        # Calculate cosine similarity using the formula: A . B / (||A|| * ||B||)
        cosSim = dot_product / (norm_A * norm_B)
    else:
        # If one or both vectors are zero vectors, cosine similarity is often
        # considered to be 0 or undefined. We'll return 0.0 as per common practice.
        cosSim = 0.0

    return np.round(cosSim, 3)


# cosine similarity = A.B /|A||B|