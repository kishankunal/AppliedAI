#https://www.scaler.com/academy/mentee-dashboard/class/417079/homework/problems/25962?navref=cl_tt_lst_nm

import numpy as np
# 1. Import decision trees for regression
from sklearn.tree import DecisionTreeRegressor

x = np.asarray(eval(input()))
y = np.asarray(eval(input()))
m = int(input())  # number of trees
lr = eval(input())


def fit(x, y, m, learning_rate):
    """
    x : attributes
    y : target variable
    m : number of decision trees
    learning_rate : learning rate
    """

    # list consisting of weak Decision trees regressors
    weak_learners = []

    # 2. Initialize the predictions with stage 0 predictions (mean of y)
    y_mean = np.mean(y)
    predictions = [y_mean] * len(y)

    # Iterating over the number of estimators
    for _ in range(0, m):
        # 3. Calculating the residuals (Actual - Current Prediction)
        residuals = [y[i] - predictions[i] for i in range(len(y))]

        # Creating a weak learner (usually a shallow tree/stump)
        weak_learner = DecisionTreeRegressor(max_depth=1)

        # 4. Training the tree on the features (x) and the residuals
        weak_learner.fit(x, residuals)

        # Appending the weak learner to the list
        weak_learners.append(weak_learner)

        # Getting the weak learner predictions for each observation
        # reshape(1,-1) is used because predict() expects a 2D array
        predictions_wl = [weak_learner.predict(i.reshape(1, -1))[0] for i in x]

        # 5. Updating current predictions: pred = pred + (lr * residual_pred)
        predictions = [predictions[i] + learning_rate * predictions_wl[i] for i in range(len(x))]

    return predictions


# Training the model and printing the final predictions for evaluation
print(fit(x, y, m, lr))