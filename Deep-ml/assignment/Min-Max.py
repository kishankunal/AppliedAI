# https://www.scaler.com/academy/mentee-dashboard/class/415561/homework/problems/20863?navref=cl_tt_lst_nm

import numpy as np


def min_max(arr):
    arr_min = np.min(arr)
    arr_max = np.max(arr)

    diff_arr = arr_max - arr_min

    if diff_arr == 0:
        norm_arr = np.zeros_like(arr, dtype=float)
    else:
        norm_arr = (arr - arr_min) / diff_arr

    return np.round(norm_arr, 2)