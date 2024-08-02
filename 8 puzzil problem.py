from heapq import heappop, heappush
from copy import deepcopy
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def calculate_manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = divmod(state[i][j] - 1, 3)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance
def a_star_search(initial_state):
    open_list = []
    heappush(open_list, (0 + calculate_manhattan(initial_state), 0, initial_state, []))
    closed_list = set()
    while open_list:
        _, g, current_state, path = heappop(open_list)
        if current_state == goal_state:
            return g, path + [current_state]
        closed_list.add(tuple(map(tuple, current_state)))
        blank_row, blank_col = find_blank(current_state)
        for move in moves:
            new_row, new_col = blank_row + move[0], blank_col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = deepcopy(current_state)
                new_state[blank_row][blank_col], new_state[new_row][new_col] = \
                    new_state[new_row][new_col], new_state[blank_row][blank_col]
                if tuple(map(tuple, new_state)) not in closed_list:
                    heappush(open_list, (g + 1 + calculate_manhattan(new_state), g + 1, new_state, path + [current_state]))
    return -1, []
def print_state(state):
    for row in state:
        print(' '.join(str(tile) if tile != 0 else ' ' for tile in row))
    print()
initial_state = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]
steps, path = a_star_search(initial_state)
if steps == -1:
    print("No solution exists.")
else:
    print(f"Number of steps to reach the goal state: {steps}")
    print("Steps to solve the puzzle:")
    for step in path:
        print_state(step)
