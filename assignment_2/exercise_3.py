# First create a class with the python list.
class List(list):

    def __getitem__(self, key):
        '''
        Overide the __getitem__ list function which is called when using brackets "[]".
        If a tupple is given as an argument, handle the case in this function.
        Otherwise, act as a regular list.
        '''
        if type(key) is tuple:
            self_copy = self.copy()
            for item in key:
                if type(self_copy) is int or item >= len(self_copy):
                    # Raise an exception.
                    raise Exception("Check the arguments.")
                else:
                    self_copy = self_copy[item]
            return self_copy
        return list(self)[key]

# Example of List (which is not a regular python list).   
mylist = List([
    [[1, 2, 3, 33], [4, 5, 6, 66]],
    [[7, 8, 9, 99], [10, 11, 12, 122]],
    [[13, 14, 15, 155], [16, 17, 18, 188]]
])

'''
Running examples
'''

if __name__ == '__main__':
    print(mylist[0])
    print(mylist[0, 1, 3])
    print(mylist[0, 1])
    print(mylist[0])
    print(mylist[1])
    print(mylist)

    try:
        print(mylist[10, 10])
    except Exception as error:
        print('error')
        
    try:
        print(mylist[0, 1, 3, 4])
    except Exception as error:
        print('error')
