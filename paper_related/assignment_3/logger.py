def constraints(constraints):
    print('\n'.join(['Agent {0} bundle size = {1}'.format(i, constraints[i]) for i in range(len(constraints))]))


def agents_valuations(agents_valuations):
    for agent in range(len(agents_valuations)):
        print('Agent {0}'.format(agent))
        for i in range(len(agents_valuations[agent])):
            print('     Object {0} : {1}'.format(i, agents_valuations[agent][i]))


def ip(agents_valuations, constraints, is_bounded=True):
    if is_bounded:
        if len(constraints) != 0:
            print('Minimize 0, \nsubject to,')
            for i in range(len(agents_valuations)):
                print(' + '.join(['x_{1}{0} * {2}'.format(i, j, agents_valuations[i][j]) for j in range(len(agents_valuations[i]))]), end='')
                print(' = {0}'.format(constraints[i]))
            for i in range(len(agents_valuations[0])):
                print('{0} = 1'.format(' + '.join(['x_{0}{1} '.format(i, j) for j in range(len(agents_valuations))])))
        else:
            print('There is no constraints.')
    else:
        print('Minimize x, \nsubject to, x > 1')

    