from copy import deepcopy
# deepcopy allows us to pass
# arrays as function arguments
# by value instead of reference

# array of solutions
queens = []

# generate new row, marking unthreatened rows
# with 0 and threatened rows as 1
def legalize(past):
    row = [0 for i in range(8)]
    for p_row in range(len(past)):
        for i in range(len(past[p_row])):
            if past[p_row][i] == "Q":
                row[i] = 1
                if i - (len(past) - p_row) >= 0:
                    row[i - (len(past) - p_row)] = 1
                if i + (len(past) - p_row) <= 7:
                    row[i + (len(past) - p_row)] = 1
    return row

def eight_queens(past=None):
    if past is None:
        past = []
        past += [[1 for i in range(8)]]
        for i in range(8):
            past[0][i] = "Q"
            eight_queens(deepcopy(past))
            past[0][i] = 1
    else:
        if len(past) == 8:
            queens.append(deepcopy(past))
        new_row = deepcopy(legalize(deepcopy(past)))
        for n_row in range(len(new_row)):
            if new_row[n_row] == 0:
                new_row[n_row] = "Q"
                #print(new_row)
                eight_queens(deepcopy(past) + [deepcopy(new_row)])
                new_row[n_row] = 0


eight_queens()


print(len(queens))
