from collections import deque

# Define the initial environment and vacuum cleaner position
initial_state = {
    'vacuum': (0, 0),
    'grid': [
        ['C', 'D', 'C'],
        ['D', 'C', 'D'],
        ['C', 'C', 'C']
    ]
}

def is_goal(state):
    for row in state['grid']:
        if 'D' in row:
            return False
    return True

def get_successors(state):
    successors = []
    vacuum_pos = state['vacuum']
    grid = state['grid']
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for direction in directions:
        new_pos = (vacuum_pos[0] + direction[0], vacuum_pos[1] + direction[1])
        if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols:
            new_grid = [row[:] for row in grid]
            if new_grid[new_pos[0]][new_pos[1]] == 'D':
                new_grid[new_pos[0]][new_pos[1]] = 'C'
            successors.append({'vacuum': new_pos, 'grid': new_grid})

    return successors

def solve(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        state_tuple = (state['vacuum'], tuple(tuple(row) for row in state['grid']))

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if is_goal(state):
            return path + [state]

        for successor in get_successors(state):
            queue.append((successor, path + [state]))

    return None

def print_solution(solution):
    for step in solution:
        vacuum_pos = step['vacuum']
        grid = step['grid']
        print(f"Vacuum at {vacuum_pos}")
        for row in grid:
            print(' '.join(row))
        print()

solution = solve(initial_state)

if solution:
    print_solution(solution)
else:
    print("No solution found.")
