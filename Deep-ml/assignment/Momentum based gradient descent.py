# https://www.scaler.com/academy/mentee-dashboard/class/441686/assignment/problems/17867?navref=cl_tt_lst_nm

# objective function used for gradient descent is (x-1)²
# x-> input value

def obj_func(x):
    return (x * x - 2 * x + 1)


# code starts here

"""
set value of 'alpha' as 0.01 and 'beta' as 0.9
"""
alpha = 0.01
beta = 0.9


def grad(x):
    # return the gradient of the objective function: d/dx of (x-1)^2 is 2*(x-1)
    return 2 * (x - 1)


"""
set value of iterations to 4
"""
iterations = 4


# function of momentum based gradient descent
def momentum(x):
    # initialize value of v to zero
    v = 0
    for i in range(iterations):
        # update the value of v on every iteration using the given formula
        # v(t+1) = beta*v(t) + (1-beta)*grad(x)
        v = beta * v + (1 - beta) * grad(x)

        # update the value of x on every iteration using the given formula
        # x(t+1) = x(t) - alpha*v(t+1)
        x = x - alpha * v

    # finally return the value of x and obj_func(x) rounded off to 2 decimal places
    return round(x, 2), round(obj_func(x), 2)

# code ends here