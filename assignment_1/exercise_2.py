import collections

def print_sorted(struct):
    if not hasattr(struct, '__iter__') or struct.__class__ == "".__class__:
        print(struct, end = ', ')
    else:
        if struct.__class__ == dict().__class__:
            for key, value in collections.OrderedDict(sorted(struct.items())).items():
                print(key, end = ', ')
                print_sorted(value)
        else:
            for item in sorted(struct):
                print_sorted(item)

'''
Tests
'''

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