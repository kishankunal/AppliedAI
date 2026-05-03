# https://www.scaler.com/academy/mentee-dashboard/class/433133/homework/problems/27156?navref=cl_tt_nv

# import SVM classifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.25)



best_support_vectors = None

# YOUR CODE GOES HERE

max_acc = 0
for kernel in kernal_list:
    for C in c_list:
        model = SVC(kernel=kernel, C=C).fit(X_train, y_train)
        model_pred = model.predict(X_test)
        acc = accuracy_score(y_test, model_pred)
        if acc > max_acc:
            max_acc = acc
            best_support_vectors = len(model.support_) # model keeps the support vectors in this parameter

# YOUR CODE ENDS HERE

print(best_support_vectors)