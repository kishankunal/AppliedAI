# https://www.scaler.com/academy/mentee-dashboard/class/417091/assignment/problems/29677?navref=cl_tt_nv

import numpy as np
np.random.seed(2)

#independent variables
X = np.array(eval(input()))
#dependent variable
y = np.array(eval(input()))

m = X.shape[0]  #no. of samples
n = X.shape[1]  #no. of features
c = len(np.unique(y)) #no. of classes in the data and therefore no. of neurons in the layer

#weight vector of dimension (number of features, number of neurons in the layer)
w = np.random.randn(n, c)

#bias vector of dimension (1, number of neurons in the layer)
b = np.zeros((1, c))

#(weighted sum + bias) of dimension (number of samples, number of classes)
z = np.dot(X, w) + b

#exponential transformation of z
a = np.exp(z)

#Perform the softmax on a
a = a / np.sum(a, axis=1, keepdims=True)

#calculate the label for each observation
y_hat = np.argmax(a, axis=1)

print(y_hat)