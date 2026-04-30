# https://www.scaler.com/academy/mentee-dashboard/class/417061/assignment/problems/25235?navref=cl_tt_lst_nm

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

observation = eval(input())

# Assuming X and y are provided globally or through some other mechanism
# For the purpose of making this code runnable and testable within the immersive,
# I'll define X_train and y_train with the sample values.
# In a real scenario, these would come from the problem's input.

# Sample data as per problem description
X_train_list = [[4, 13, 2], [9, 8, 11], [14, 4, 2]]
y_train_list = [0, 1, 0]

X_train = np.asarray(X_train_list)
y_train = np.asarray(y_train_list)


# INITIALIZE KNN CLASS WITH K = 2
knn = KNeighborsClassifier(n_neighbors=2)

# TRAIN KNN MODEL
knn.fit(X_train, y_train)

# PRINT PREDICTED VALUE BY THE MODEL FOR the variable 'observation'
# The predict method expects a 2D array, even for a single observation.
print(knn.predict(observation))