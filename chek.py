import random

x = ['x', 'x', 'x', 'x', 'yes', 'x', 'x', 'x', 'x', 'x', 'yes', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'yes', 'x',
     'x', 'yes', 'x', 'x', 'x', 'yes', 'x', 'x', 'yes', 'x', 'x', 'x', 'yes', 'x', 'x', 'x', 'x']
y = ['x']
q_count = 3


def chek(i):
    if i in y:
        print('not found')
        return chek(random.choice(x))
    else:
        return i


for i in range(q_count):
    print(chek(x[i]))
