# https://www.scaler.com/academy/mentee-dashboard/class/433133/assignment/problems/15859?navref=cl_tt_lst_nm
from sklearn.metrics import hinge_loss
import numpy as np


# $$Loss = \frac{1}{N} \sum_{i=1}^{N} \max(0, 1 - y_i \cdot f(x_i))$$

def compute_loss(W, X, Y):
    # w is weight vector
    # x is input vector
    # y is dependent variable
    # calculate hinge loss
    N = X.shape[0]

    f_x = X * W

    distance_from_margin = 1 - (Y * f_x)

    individual_losses = np.maximum(0, distance_from_margin)

    hinge_loss = sum(individual_losses)/N

    # enter your code here
    return hinge_loss


