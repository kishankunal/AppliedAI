# https://www.scaler.com/academy/mentee-dashboard/class/415546/homework/problems/23467?navref=cl_tt_lst_nm

import numpy as np


def logloss(z, y_true, x):

    z = np.asarray(z)
    y_true = np.asarray(y_true)
    x = np.asarray(x)

    epsilon = 1e-10
    y_hat = 1 / (1 + np.exp(-z))


    y_hat = np.clip(y_hat, epsilon, 1 - epsilon)

    log_loss_values = -y_true * np.log(y_hat) - (1 - y_true) * np.log(1 - y_hat)

    derivative_values = (y_hat - y_true) * x[:, 0]

    return np.round(log_loss_values, 2), np.round(derivative_values, 2)