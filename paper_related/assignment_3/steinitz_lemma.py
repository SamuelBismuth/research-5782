from operator import le
import numpy as np

def prepare_to_lemma(agents_valuations, constraints):
    z_norm = np.linalg.norm(agents_valuations)
    arranged_A = []
    for i in range(len(agents_valuations)):
        arranged_A.append(np.subtract(agents_valuations[i], constraints[i]/z_norm))
    # print(agents_valuations)
    # print(constraints)
    # print(z_norm)
    # print(arranged_A)
    '''
    You can see that both equations are actually the same!
    We can now apply the lemma.
    '''
    apply_lemma(arranged_A)


def apply_lemma(arranged_A):
    '''
    Maybe we should use the initial equation to keep everything clean.
    '''
    print('We can now apply the Steinitz Lemma.')
