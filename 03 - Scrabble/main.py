import itertools

TOTAL = 46
NUM_TILES = 7

answer = 0

# CBA to type out 100 tiles
tiles_data = [   {"letter" : 'A', "value" : 1, "numberof": 9},
            {"letter" : 'B', "value" : 3, "numberof": 2},
            {"letter" : 'C', "value" : 3, "numberof": 2},
            {"letter" : 'D', "value" : 2, "numberof": 4},
            {"letter" : 'E', "value" : 1, "numberof": 12},
            {"letter" : 'F', "value" : 4, "numberof": 2},
            {"letter" : 'G', "value" : 2, "numberof": 3},
            {"letter" : 'H', "value" : 4, "numberof": 2},
            {"letter" : 'I', "value" : 1, "numberof": 9},
            {"letter" : 'J', "value" : 8, "numberof": 1},
            {"letter" : 'K', "value" : 5, "numberof": 1},
            {"letter" : 'L', "value" : 1, "numberof": 4},
            {"letter" : 'M', "value" : 3, "numberof": 2},
            {"letter" : 'N', "value" : 1, "numberof": 6},
            {"letter" : 'O', "value" : 1, "numberof": 8},
            {"letter" : 'P', "value" : 3, "numberof": 2},
            {"letter" : 'Q', "value" : 10, "numberof": 1},
            {"letter" : 'R', "value" : 1, "numberof": 6},
            {"letter" : 'S', "value" : 1, "numberof": 4},
            {"letter" : 'T', "value" : 1, "numberof": 6},
            {"letter" : 'U', "value" : 1, "numberof": 4},
            {"letter" : 'V', "value" : 4, "numberof": 2},
            {"letter" : 'W', "value" : 4, "numberof": 2},
            {"letter" : 'X', "value" : 8, "numberof": 1},
            {"letter" : 'Y', "value" : 4, "numberof": 2},
            {"letter" : 'Z', "value" : 10, "numberof": 1},
            {"letter" : ' ', "value" : 0, "numberof": 2},    ]

tiles = []
for tile in tiles_data:
    for i in range(0,tile["numberof"]):
        tiles.append({"letter" : tile["letter"], "value" : tile["value"]})

for combination in itertools.combinations(tiles, NUM_TILES):
    sum = 0
    str = ''
    for tile in combination:
        sum += tile["value"]
        str += tile["letter"]

    if sum == TOTAL:
        answer += 1
        print(str)

print("Answer = {}".format(answer))
