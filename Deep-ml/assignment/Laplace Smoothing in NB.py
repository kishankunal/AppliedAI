# https://www.scaler.com/academy/mentee-dashboard/class/417082/homework/problems/25989/?navref=cl_pb_nv_tb

def laplaceSmoothing(nj1, n1, alpha):
    """
    nj1: occurrences of word wj in class 1
    n1: total number of samples in class 1
    alpha: smoothing parameter
    """
    # Number of categories (Present or Absent) for Bernoulli Naive Bayes
    C = 2

    # Apply Laplace Smoothing Formula: (nj1 + alpha) / (n1 + alpha * C)
    smoothed_probability = (nj1 + alpha) / (n1 + alpha * C)

    # Return the result rounded to 3 decimal places
    return round(smoothed_probability, 3)