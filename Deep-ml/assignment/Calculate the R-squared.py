# http://scaler.com/academy/mentee-dashboard/class/415543/homework/problems/25091?navref=cl_tt_lst_nm

import numpy as np


def calc_r2(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    y_true_mean = np.mean(y_true)

    tot_ss = np.sum((y_true - y_true_mean) ** 2)

    res_ss = np.sum((y_true - y_pred) ** 2)


    if tot_ss == 0:
        r2 = 1.0 if res_ss == 0 else 0.0  # If TSS is 0, and RSS is 0, it's a perfect fit (R2=1). Otherwise, 0.
    else:
        r2 = 1 - (res_ss / tot_ss)

    return np.round(r2, 2)