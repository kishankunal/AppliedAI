# https://www.scaler.com/academy/mentee-dashboard/class/433133/assignment/problems/27117?navref=cl_tt_nv

# import SVM classifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def tune_params(X, y, kernel_list, c_list):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.25)

    best_kernel = None
    best_C = None

    max_acc = 0
    for kernel in kernel_list:
        for C in c_list:
            model = SVC(kernel=kernel, C=C).fit(X_train, y_train)
            model_pred = model.predict(X_test)
            acc = accuracy_score(y_test, model_pred)
            if acc > max_acc:
                max_acc = acc
                best_kernel, best_C = kernel, C

    return best_kernel, best_C