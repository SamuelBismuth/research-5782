# First create a class with the python list.
class List(list):

    def __getitem__(self, key):
        '''
        Overide the __getitem__ list function which is called when using brackets "[]".
        If a tupple is given as an argument, handle the case in this function.
        Otherwise, act as a regular list.
        '''
        string_exec = 'self'
        if hasattr(key, '__iter__'):
            for item in key:
                string_exec = string_exec + '[{0}]'.format(item)
        else:
            return list(self)[key]
        return eval(string_exec)

    
    def __setitem__(self, key, value):
        '''
        Overide the __setitem__ list function which is called when using brackets "[]".
        If a tupple is given as an argument, handle the case in this function.
        Otherwise, act as a regular list.
        '''       
        string_exec = 'self'
        if hasattr(key, '__iter__'):
            for item in key:
                string_exec = string_exec + '[{0}]'.format(item)
            string_exec = string_exec + ' = {0}'.format(value)
            exec(string_exec)
        else:
            self.pop(key)
            self.insert(key, value)
       

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
    mylist.append(5)
    print(mylist)
    print(mylist[0, 1, 3])
    print(mylist[0, 1])
    print(mylist[0])
    print(mylist[1])
    print(mylist)
    mylist[0] = 4
    print(mylist)
    mylist[0] = 9
    print(mylist)
    mylist[1] = 9
    print(mylist)
    mylist[2, 1] = 3
    print(mylist)

    try:
        mylist[0, 1, 3, 4] = 3
    except Exception as error:
        print(error)

    try:
        print(mylist[10, 10])
    except Exception as error:
        print(error)
        
    try:
        print(mylist[0, 1, 3, 4])
    except Exception as error:
        print(error)
