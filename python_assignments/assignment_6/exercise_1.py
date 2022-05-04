from typing import Callable
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


def plotIntersection(t: np.ndarray, f: Callable, g: Callable):
    """
    This method receives two functions and create a plot with both functions and the intersection points between the functions.
    
    >>> f = lambda x : x**2
    >>> g = lambda x : x+10
    >>> plotIntersection(np.linspace(-10, 10, 1000), f, g)

    >>> f = lambda x : np.sin(x)
    >>> g = lambda x : 0.2*x
    >>> plotIntersection(np.linspace(-10, 10, 1000), f, g)

    >>> f = lambda x : x**3
    >>> g = lambda x : x-10
    >>> plotIntersection(np.linspace(-10, 10, 1000), f, g)

    >>> f = lambda x : x+2
    >>> g = lambda x : x-2
    >>> plotIntersection(np.linspace(-10, 10, 1000), f, g)

    >>> f = lambda x : x
    >>> g = lambda x : x-11
    >>> plotIntersection(np.linspace(0, 10, 1000), f, g)

    >>> f = lambda x : -x
    >>> g = lambda x : x
    >>> plotIntersection(np.linspace(0, 10, 1000), f, g)

    >>> f = lambda x : -x
    >>> g = lambda x : x
    >>> plotIntersection(np.linspace(-10, 10, 1000), f, g)

    >>> f = lambda x : np.sin(x)
    >>> g = lambda x : -np.sin(x)
    >>> plotIntersection(np.linspace(1, 10, 100), f, g)

    >>> f = lambda x : np.sin(x)
    >>> g = lambda x : np.cos(x)
    >>> plotIntersection(np.linspace(1, 10, 100), f, g)
    """
    intersections = set()
    for i in t:
        intersections.add(float(format(float(fsolve(lambda x : f(x) - g(x), i)), '.4f')))
    
    intersections = list(intersections)

    cleaned_intersections = []
    for intersection in intersections:
        if intersection >= t[0] and intersection <= t[len(t)-1]:
            if (f(intersection) - g(intersection)) < 0.05 and (f(intersection) - g(intersection)) > -0.05:
                cleaned_intersections.append(intersection)

    x_coordinates = cleaned_intersections
    y_coordinates = [f(cleaned_intersections[i]) for i in range(len(cleaned_intersections))]

    plt.plot(t, f(t), 'b')
    plt.plot(t, g(t), 'g')
    plt.scatter(x_coordinates, y_coordinates)
    plt.show()


if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))