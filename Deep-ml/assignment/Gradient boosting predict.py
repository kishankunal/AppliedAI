#https://www.scaler.com/academy/mentee-dashboard/class/417079/assignment/problems/25938?navref=cl_tt_nv
import numpy as np

def gbdt_predict(weak_learners, learning_rate, X_test, y_mean):
    """
    Given the list of weak_learners and learning rate use the trained decision trees to predict the response variable for the observations in x
    """

    # initialize the output with stage 0 prediction
    yhat = np.full(len(X_test), y_mean)

    # Calculate the output for the observations in the x according to gradient boosting's all models
    for i in range(len(weak_learners)):
        yhat += learning_rate * weak_learners[i].predict(X_test)

    return yhat