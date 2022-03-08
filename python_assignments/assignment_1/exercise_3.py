from sympy import *

# Bigger the treeshold is, better will the estimation be but longer the running time will be.
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
    
    return int(iter)


def find_derivative(f, x):
    return lambdify(x, f(x).diff(x))

'''
Running examples
'''

if __name__ == '__main__':
    print(find_root(lambda x: x**2-4, 1, 3))
    print(find_root(lambda x: x * x * x - x * x + 2, 0, 2))
    print(find_root(lambda x: x * x * x * x - x * x + 2, 0, 2))
