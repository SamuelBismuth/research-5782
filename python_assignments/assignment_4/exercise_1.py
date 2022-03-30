def combinations(iterable, r, item, C):
    '''
    This function is the combination function found in the itertools library.
    I started from this function and I stopped the iterations while the sum was to large, in order to stop useless running.
    https://stackoverflow.com/questions/5731505/where-can-i-find-source-code-for-itertools-combinations-function
    '''
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    if item + sum(tuple(pool[i] for i in indices)) > C:
        return
    yield [item] + list(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        if item + sum(tuple(pool[i] for i in indices)) > C:
            return
        yield [item] + list(pool[i] for i in indices)


def bounded_subsets(S, C) :
    '''
    This generater iterate over each item and compute every subset of size k in the alphabetical order.
    That is, from the first very moment where the sum item + combination is strictly more than C, we can pass and continue with the subset
    of size k+1. 
    In this way, no useless subsets are created.
    '''
    # We first sort the list O(n*log(n)), where n = len(S).
    S.sort()
    if S[0] < 0 or C < 0:
        raise Exception('input must be positive only.')
    # yield []
    yield []
    for index, item in enumerate(S):
        iterable = S[index+1:]
        for r in range(len(iterable) + 1):
            for subset in combinations(iterable, r, item, C):
                yield list(subset)

'''
Running examples
'''

if __name__ == '__main__':

    S = [1, 2, 3, 40, 50]
    C = 6

    for s in bounded_subsets(S, C):
        print(s)

    # Should print every subsets.
    S = [1, 20, 3, 1, 50]
    C = 100

    for s in bounded_subsets(S, C):
        print(s)

    # Should raise an exception
    S = [-1, 20, 3, 1, 50]
    C = 100

    try:
        for s in bounded_subsets(S, C):
            print(s)
    except Exception as error:
        print(error)

