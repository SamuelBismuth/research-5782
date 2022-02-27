from sympy import *

TREESHOLD = 0.001


# Assume a root exists
def find_root(f, min, max):
    x = symbols('x')
    f_derivative = find_derivative(f, x)

    iter = 1
    h = f(iter)/f_derivative(iter)

    # We can use as a stopper the given interval, but the result are depends on the given interval.
    # That is why, I prefer to use a different treeshold that is not dependent on anything.
    # while iter >= max or iter <= min:
    while h < TREESHOLD:
        h = f(iter)/f_derivative(iter)
        iter = iter - h
    
    print("The value of the root is {0}".format(iter))


def find_derivative(f, x):
    return lambdify(x, f(x).diff(x))

'''
Tests
'''

find_root(lambda x: x**2-4, 1, 3)
find_root(lambda x: x * x * x - x * x + 2, 0, 2)
