# https://www.scaler.com/academy/mentee-dashboard/class/417103/assignment/problems/25806?navref=cl_tt_nv

import numpy as np

# Assuming X and y are already provided in the environment as per the platform's setup
observation = eval(input())

"""
'observation' IS THE OBSERVATION THAT YOU HAVE TO PREDICT.
DO NOT CHANGE THE ABOVE CODE
An example of 'observation' variable: [[5,15,20]]
"""

X_train = np.asarray(X)
y_train = np.asarray(y)


# 1. IMPORT DECISION TREE CLASSIFICATION MODEL
from sklearn.tree import DecisionTreeClassifier

# 2. INITIALIZE DECISION TREE CLASSIFICATION MODEL
classifier = DecisionTreeClassifier()

# 3. TRAIN DECISION TREE CLASSIFICATION MODEL
classifier.fit(X_train, y_train)

# 4. PRINT PREDICTED VALUE BY THE MODEL FOR the variable 'observation'
# Use the predict() method which takes a 2D array (like your 'observation' variable)
print(classifier.predict(observation))