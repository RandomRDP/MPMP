from math import sqrt
from itertools import combinations,permutations

NUM_COUNTERS = 6
SIZE_X = 6
SIZE_Y = 6


class Grid(object):

    def __init__(self):
        self.Counters = []
        self.works = True

    def Add_Counter(self,x,y):
        self.Counters.append(self.Counter(x,y))

    def Calculate_Distance(self,x1,y1,x2,y2):
        x = abs(x1 - x2)
        y = abs(y1 - y2)
        return round(sqrt(x**2 + y**2),3)

    def Calculate_Distances(self):
        self.Distances = []
        for combination in combinations(self.Counters,2):
            self.Distances.append(self.Calculate_Distance(combination[0].x,combination[0].y,combination[1].x,combination[1].y))
#            print("i x:{} y:{} j x:{} y:{} k dis:{}".format(combination[0].x,combination[0].y,combination[1].x,combination[1].y,self.Distances[-1]))

    def Check_Grid(self):
        if len(self.Distances) != len(set(self.Distances)):
            self.works = False


    class Counter:
        def __init__(self,x,y):
            self.x = x
            self.y = y


l_permutations = []
for permutation in permutations(range(NUM_COUNTERS),2):
    l_permutations.append(permutation)
for i in range(0,NUM_COUNTERS-1):
    l_permutations.append((i,i))

for combination in combinations(l_permutations,NUM_COUNTERS):
    grid = Grid()

    for i in range(0,NUM_COUNTERS):
        grid.Add_Counter(combination[i][0],combination[i][1])
    grid.Calculate_Distances()
    grid.Check_Grid()

    if grid.works:
        print("works!! :) {}".format(combination))
        print(grid.Distances)
