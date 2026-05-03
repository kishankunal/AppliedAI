# https://www.scaler.com/academy/mentee-dashboard/class/433133/homework/problems/15888?navref=cl_tt_nv


import numpy as np


def svm_cost(weights, inps, labels, C):
    """
    weights: weights learned by the SVM model
    inps   : input data points
    labels : corresponding labels
    C      : Penalty parameter
    """
    cost = 0
    x = np.array(inps)
    y = np.array([1 if label == 1 else -1 for label in labels])
    weights = np.array(weights)

    # YOUR CODE GOES HERE

    # 1. Calculate L2 Regularization term: (1/2) * ||w||^2
    l2_regularization = 0.5 * np.sum(np.square(weights))

    # 2. Calculate Hinge Loss for each point: max(0, 1 - y * (w . x))
    # We assume b=0 as it is not provided in the input weights
    n = len(y)
    distances = 1 - y * (np.dot(x, weights))
    hinge_loss = np.maximum(0, distances)

    # 3. Combine using the cost function formula: J(w,b) = Regularization + (C/n) * Sum(Hinge Loss)
    cost = l2_regularization + (C / n) * np.sum(hinge_loss)

    # CODE ENDS HERE
    return round(float(cost), 3)