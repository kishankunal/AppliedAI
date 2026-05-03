#https://www.scaler.com/academy/mentee-dashboard/class/417103/homework/problems/25488?navref=cl_tt_lst_nm

from collections import Counter
import numpy as np


def gini_impurity(class_vector):
    lst = np.array(class_vector)
    _, counts = np.unique(lst, return_counts=True)
    probs = counts/len(lst)
    prob_sqrsum = np.sum(np.square(probs))
    gini_imp = 1 - prob_sqrsum
    return np.round(gini_imp, 2)