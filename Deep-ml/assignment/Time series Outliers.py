# https://www.scaler.com/academy/mentee-dashboard/class/417085/assignment/problems/27601?navref=cl_tt_nv


import numpy as np


def replace_outliers(arraySeries):
    """arraySeries is a numpy array,
       return the required numpy array"""

    mean_val = np.mean(arraySeries)
    std_val = np.std(arraySeries)  # standard deviation
    median_val = np.median(arraySeries)

    # Calculate the absolute difference of each timepoint from the series mean
    abs_diff = np.abs(arraySeries - mean_val)

    # Calculate a mask for the differences that are > 2 standard deviations from the mean
    outlier_mask = abs_diff > (2 * std_val)

    # Replace these values with the median accross the data

    arraySeries[outlier_mask] = median_val
    return arraySeries
