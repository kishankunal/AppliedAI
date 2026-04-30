# https://www.scaler.com/academy/mentee-dashboard/class/417061/homework/problems/25269?navref=cl_tt_lst_nm

import numpy as np

from sklearn.neighbors import KNeighborsClassifier

X_train = np.asarray(X)
y_train = np.asarray(y)


def findOptimalK(X_train, y_train, x_q):
    error_rate = []

    for i in range(1, 11):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        pred_i = knn.predict(x_q)
        error_rate.append(np.mean(pred_i != y_train))

    index = np.argmin(error_rate)

    return index + 1 # index starts from 0 so +1
