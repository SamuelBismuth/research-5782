def lastcall(func):
    '''
    This method is used as a decorator.
    It outputs a message if the function outputs the same thing twice in a raw. 
    '''
    lastcall.old=None
    def wrapper(arg):
        ans = func(arg)
        if ans == lastcall.old:
            print("I already told you that the answer is {0}".format(lastcall.old))
        else:
            lastcall.old = ans
            return ans
    return wrapper    
    

# Functions to test the decorator.

@lastcall
def f(x:int):
    return x**2

@lastcall
def h(y:int):
    return y*2

@lastcall
def mysplit(string:str):
    return string.split(' ')


'''
Running examples
'''

if __name__ == '__main__':
    f(2)
    # Already told you.
    f(2)
    f(3)
    f(4)
    # Already told you.
    f(4)
    f(2)

    h(5)
    # Already told you.
    h(5)
    h(3)
    h(4)
    # Already told you.
    h(4)
    h(2)

    mysplit('sam uel')
    # Already told you.
    mysplit('sam uel')
    mysplit('er el')
    mysplit('simon')
    # Already told you.
    mysplit('bismuth')
    mysplit('bismuth')