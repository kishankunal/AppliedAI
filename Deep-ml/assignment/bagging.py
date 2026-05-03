# https://www.scaler.com/academy/mentee-dashboard/class/417088/assignment/problems/25809?navref=cl_tt_nv


import numpy as np
from sklearn.tree import DecisionTreeClassifier

np.random.seed(0)

train = np.asarray(eval(input()))
test = np.asarray(eval(input()))
max_depth = int(input())  # maximum depth of trees
n_trees = int(input())  # number of trees
ratio = float(input())  # ratio of length of dataset to be generated while sampling


# Construct a tree model with max_depth = "max_depth", train it on the sample and return the model
def build_tree(sample, max_depth):
    tree = DecisionTreeClassifier(max_depth=max_depth)
    sample = np.asarray(sample)
    X_sample = sample[:,:-1]
    y_sample = sample[:,-1]
    tree.fit(X_sample, y_sample)
    return tree


def bagging_predict(trees, row):
    # predictions is the list of labels predicted by all the trees
    predictions = [tree.predict(row.reshape(1, -1))[0] for tree in trees]

    # return the prediction according to procedure used in bagging in classification
    return max(set(predictions), key=predictions.count)


# bagging
def bagging(train, test, max_depth, n_trees, ratio):
    trees = list()
    for i in range(n_trees):
        sample = subsample(train, ratio)  # A sample created from dataset of size round(len(dataset) * ratio)
        tree = build_tree(sample, max_depth)
        trees.append(tree)

    # store the predictions for each observation in the test data
    predictions = [int(bagging_predict(trees, row)) for row in test]
    return (predictions)