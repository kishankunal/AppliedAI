#https://www.scaler.com/academy/mentee-dashboard/class/417079/assignment/problems/25971?navref=cl_tt_nv
import numpy as np
try:
    observation = eval(input())

    X_train = np.asarray(X)
    y_train = np.asarray(y)

    # IMPORT GRADIENT BOOSTING CLASSIFIER
    from sklearn.ensemble import GradientBoostingClassifier

    # INITIALIZE GRADIENT BOOSTING CLASSIFIER
    classifier = GradientBoostingClassifier(random_state=0)

    # TRAIN GRADIENT BOOSTING CLASSIFIER
    classifier.fit(X_train, y_train)

    # PRINT PREDICTED VALUE BY THE MODEL FOR the variable 'observation'
    print(classifier.predict(observation))

except:
    pass

