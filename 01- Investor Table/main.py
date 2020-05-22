from itertools import permutations

SIZE_TABLE = 7
MIN_NUM_CORRECT = 2

peeps = list(range(SIZE_TABLE))


def test_table(t_peeps):
    t_seats = list(range(SIZE_TABLE))
    for i in range(0,SIZE_TABLE):
        t_seats.append(t_seats.pop(0))
        if test_rotation(t_peeps,t_seats):
            return True
    return False

def test_rotation(r_peeps, r_seats):
    num_correct = 0
    for i, peep in enumerate(r_peeps):
        if peep == r_seats[i]:
            num_correct += 1
    if num_correct >= MIN_NUM_CORRECT:
        return True
    else:
        return False

for permutation in list(permutations(peeps)):
    if not test_table(permutation):
        print(permutation)
