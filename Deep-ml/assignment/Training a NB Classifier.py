# https://www.scaler.com/academy/mentee-dashboard/class/417082/assignment/problems/26055?navref=cl_tt_nv

# Import Multinomial naive bayes from the appropriate library
from sklearn.naive_bayes import MultinomialNB

# Import accuracy_score from the appropriate library
from sklearn.metrics import accuracy_score


# Define train_and_predict()
def train_and_predict(alpha):
    # Instantiate the classifier: nb_classifier, and plug in alpha's value
    nb_classifier = MultinomialNB(alpha=alpha)

    # Fit to the training data
    nb_classifier.fit(X_train, y_train)

    # Predict the labels: pred
    pred = nb_classifier.predict(X_test)

    # Compute accuracy: score
    score = accuracy_score(y_test, pred)

    return score


# Iterate over the alphas and print the corresponding score
for alpha in alphas:
    print('Alpha: ', alpha)
    # Call the function to get the score for the current alpha
    print('Score: ', train_and_predict(alpha))
    print()