# https://www.scaler.com/academy/mentee-dashboard/class/417103/assignment/problems/25764?navref=cl_tt_lst_nm

import numpy as np


def entropy(y_target):
    '''
    Calculates the entropy given list of target(binary) variables
    '''

    np_y = np.array(y_target)

    if len(np_y) == 0:
        return 0

    entropy = 0

    # calculate the counts of each unique element in the

    _, counts = np.unique(np_y, return_counts=True)

    # Probabilities of each class label
    prob = counts/len(np_y)
    epsilon = 1e-9

    entropy = np.sum(prob * np.log2(prob + epsilon))

    return np.round(-entropy, 2)