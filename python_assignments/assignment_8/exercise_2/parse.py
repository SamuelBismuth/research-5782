import numpy as np


def parse_c_A_b(lines):
    '''
    This method parse the lines of the sheet into some np arrays.
    '''
    index_A = [i[0] for i in lines].index('A=')
    index_b= [i[0] for i in lines].index('b=')
    index_c = [i[0] for i in lines].index('c=')
    
    A =  np.array(lines[index_A+1:index_b], dtype=np.int8)
    b =  np.array(lines[index_b+1], dtype=np.int8)
    c =  np.array(lines[index_c+1], dtype=np.int8)

    return c, A, b
