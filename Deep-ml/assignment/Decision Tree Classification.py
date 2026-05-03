#https://www.scaler.com/academy/mentee-dashboard/class/417103/assignment/problems/17484?navref=cl_tt_nv
import numpy as np


def entropy(s):
    '''
    Calculates the entropy given list of target(binary) variables
    '''
    # Write your code here

    # Caclulate entropy
    s = np.array(s)
    if len(s) == 0:
        return 0

    _, count = np.unique(s, return_counts=True)

    prob = count / len(s);
    entropy = np.sum(prob * np.log2(prob + 1e-15))

    return -entropy


def information_gain(parent, left_child, right_child):
    '''
    Compute information gain given left_child target variables (list), right_child target variables(list) and their parent targets(list)
    '''
    parent_entropy = entropy(parent)

    n_total = len(parent)
    n_left = len(left_child)
    n_right = len(right_child)

    wieghted_child_entropy = (n_left / n_total) * entropy(left_child) + (n_right / n_total) * entropy(right_child)

    info_gain = parent_entropy - wieghted_child_entropy

    return info_gain


def best_split(features, labels):
    '''
    inputs:
        features: nd-array
        labels: nd-array
    output:
        float value determining best threshold for decision tree classification
    '''

    best_threshold = None
    best_info_gain = -1

    # For every unique value of that feature
    for threshold in np.unique(features):

        mask = features <= threshold
        y_left = labels[mask]
        y_right = labels[~mask]

        if len(y_left) > 0 and len(y_right) > 0:
            gain = information_gain(labels, y_left,
                                    y_right)  # Caclulate the information gain and save the split parameters if the current split if better then the previous best

            if gain > best_info_gain:
                best_threshold = threshold
                best_info_gain = gain

    return best_threshold