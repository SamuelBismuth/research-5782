import numpy as np
import constant as CONSTANT
import logger

import steinitz_lemma as steinitz

''' 
Since IP includes almost every combinatorial problems, we chosed to focus on PROPWithSharedObject(n,s) problem instance.
Given n agents PROPWithSharedObject problem decides if there exists a proportionnal division of m objects
among the n agents sharing s object.

There are two intuitive cases in our problem. The first one is when the agents valuate the objects similarly.
The second is when there are different valuations over the objects.

During our thesis work, we proved that it is always optimal to share the biggest objects. 
Then, we can put the s biggest objects aside, and get focus on the other objects.

We will provide running example for the identical valuations case. 
In the future using mixed integer programming, it will be interesting to check the running time of the problem 
PROPWithSharedObject(n,s) with different valuation. We will also be able to see which object the solver decides to share.
'''

def compute_agents_equal_valuations_uniform(n, m):
    return [np.random.randint(CONSTANT.MIN_VALUATION, CONSTANT.MAX_VALUATION, [m])]*n


def compute_agents_equal_valuations_poisson(n, m):
    return [np.random.poisson(CONSTANT.MIN_VALUATION, CONSTANT.MAX_VALUATION, [m])]*n


def compute_prop_constraints(agents_valuations):
    return [sum(agent)/len(agents_valuations) for agent in agents_valuations]


def random_example_equal_valuations(n, m, is_uniform = True):
    if is_uniform:
        agents_valuations = compute_agents_equal_valuations_uniform(n, m)
    else:
        agents_valuations = compute_agents_equal_valuations_poisson(n, m)
    constraints = compute_prop_constraints(agents_valuations)
    logger.agents_valuations(agents_valuations)
    logger.constraints(constraints)
    logger.ip(agents_valuations, constraints)
    steinitz.prepare_to_lemma(agents_valuations, constraints)


def fixed_example_equal_valuations(agents_valuations):
    constraints = compute_prop_constraints(agents_valuations)
    logger.agents_valuations(agents_valuations)
    logger.constraints(constraints)
    logger.ip(agents_valuations, constraints)
    steinitz.prepare_to_lemma(agents_valuations, constraints)


def unbounded_example():
    agents_valuations = compute_agents_equal_valuations_uniform(2, 1)
    constraints = compute_prop_constraints(agents_valuations)
    logger.ip(agents_valuations, constraints, is_bounded=False)


if __name__ == '__main__':

    '''
    Fixed examples.
    '''
    # print('first simple examples')

    # fixed_example_equal_valuations([[2, 3],[2, 3]])
    # ''' As ouput, we should have no solution since the agent with the object '2' will envy the agent with the object '3'.'''

    print('second simple examples')

    fixed_example_equal_valuations([[3, 3],[3, 3]])
    ''' As ouput, there are two solutions: either x_00 = 1, x_10 = 0, x_11 = 1, x_10=0 or x_00 = 0, x_10 = 1, x_11 = 0, x_10=1. '''

    # print('third simple examples')

    # fixed_example_equal_valuations([[2, 3, 5],[2, 3, 5]])
    # ''' As ouput, we should have one agent with object '2' and '3' and the second agent with object '5' '''
    # ''' 2+3=5 '''

    # '''First random simple example to start with'''
    # random_example_equal_valuations(2, 2)

    # '''We first do some random example starting from easy instance to hardest instance due to the amount of agents and objects.'''
    # print('####################################')
    # print('####################################')
    # print('Random example (uniform distribution).')
    # for n in range(1, 5, 1):
    #     m = np.random.randint(20)
    #     print('####################################')
    #     print('Simple example: {0} agents, {1} object.'.format(n, m))
    #     random_example_equal_valuations(n, m)
    # for n in range(5, 50, 10):
    #     m = np.random.randint(50)
    #     print('####################################')
    #     print('Average example: {0} agents, {1} object.'.format(n, m))
    #     random_example_equal_valuations(n, m)
    # for n in range(50, 550, 100):
    #     m = np.random.randint(100)
    #     print('####################################')
    #     print('Hard example: {0} agents, {1} object.'.format(n, m))
    #     random_example_equal_valuations(n, m)
    # print('####################################')
    # print('####################################')

    # ''' Second, we trigger the if of the algorithm '''
    # print('Not feasible example')
    # random_example_equal_valuations(n=2, m=1)
    # print('####################################')
    # print('Unbounded example')
    # ''' By definition of our problem, there is no unbounded example then, we make another instance. '''
    # unbounded_example()
    # print('####################################')

    # ''' Finaly, we check edge cases'''
    # print('####################################')
    # print('Non sense example')
    # random_example_equal_valuations(n=0, m=0)
    # print('####################################')
    # print('Big number of agents, small number of objects')
    # random_example_equal_valuations(n=100000, m=2)
    # print('####################################')
    # print('Big number of objects, small number of agents')
    # random_example_equal_valuations(n=2, m=1000000)
    # print('####################################')
    # print('Big number of agents, big number of objects')
    # random_example_equal_valuations(n=100000, m=200000)
    # print('Poisson distribution')
    # random_example_equal_valuations(n=10, m=20)


   