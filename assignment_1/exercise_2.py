import collections

def print_sorted(struct):
    # If the struct is not iterable or if you are a string, print.
    if not hasattr(struct, '__iter__') or struct.__class__ == "".__class__:
        print(struct, end = ',')
    else:
        # We differentiate dict from other data structure.
        if struct.__class__ == dict().__class__:
            print('{', end = '')
            # We use the lambda expression to order by alphabetical order to handle case like ((9, 8), 7)
            for key, value in collections.OrderedDict(sorted(struct.items(), key = lambda x: str(x))).items():
                print_sorted(key)
                print(end = ':')
                print_sorted(value)
            print('} ', end = '')
        else:
            print('(', end = '')
            for item in sorted(struct, key = lambda x: str(x)):
                print_sorted(item)
            print(')', end = ',')


'''
Tests
'''

x = {"a":5, "c":6, "b":[(1, 3, 2, 5, 4), 3, 2, 4]}
print_sorted(x)
print()

x = {"a":5, (3, (3, 1)):(8, 4, 3), "b":[(1, 3, 2, 5, 4), 3, 2, 4]}
print_sorted(x)
print()

x = (3, [4, 3, 2], 9)
print_sorted(x)
print()

x = {"a":5, "c":6, "b":[1, 3, 2, 4]}
print_sorted(x)
print()

x = {"a":5, "c":6, "b":{"a":5, "c":6, "b":[1, 3, 2, 4]}}
print_sorted(x)
print()

x = {"a":5, "c":set(["A", "b", "a"]), "b":[9, 3, 2, 4]}
print_sorted(x)
print()

x = {"a":5, "c":set(["A", "b", "a"]), "b":(9, 3, 2, 4)}
print_sorted(x)
print()

x = [1, 2, 4, 3, 2]
print_sorted(x)
print()

x = set([1, 2, 4, 3, 2])
print_sorted(x)
print()

x = (1, 2, 4, 3, 2)
print_sorted(x)
print()