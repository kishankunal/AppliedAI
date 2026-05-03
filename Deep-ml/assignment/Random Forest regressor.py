# https://www.scaler.com/academy/mentee-dashboard/class/417088/assignment/problems/25822?navref=cl_tt_nv

"""
X_train --> Training data containing features
y_train --> Training data containing lables
X_test --> Testing data of containing features
"""

import numpy as np
np.random.seed(0)

#import random forest for regression
from sklearn.ensemble import RandomForestRegressor

#create regressor object with 5 trees
regressor = RandomForestRegressor(n_estimators=5, random_state=0)

#train the model on the training data
regressor.fit(X_train, y_train)

#calculate the predictions for the observations in the test data and round off to 2 decimal places
pred = np.round(regressor.predict(X_test),2)

print(pred)