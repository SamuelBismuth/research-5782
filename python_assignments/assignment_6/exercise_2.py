def plotIntersection():
    """
    >>> f = lambda x : x**2
    >>> g = lambda x : x+10
    >>> plotIntersection(np.linspace(-10, 10, 1000, f, g)
    array([33. , 33.1])
    """




if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))