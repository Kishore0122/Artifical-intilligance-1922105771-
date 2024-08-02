from collections import deque

def is_valid(state):
    M1, C1, B, M2, C2 = state
    if M1 < 0 or C1 < 0 or M2 < 0 or C2 < 0:
        return False
    if M1 > 0 and M1 < C1:
        return False
    if M2 > 0 and M2 < C2:
        return False
    return True

def get_successors(state):
    M1, C1, B, M2, C2 = state
    successors = []
    if B == 1:
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for move in moves:
            new_state = (M1 - move[0], C1 - move[1], 0, M2 + move[0], C2 + move[1])
            if is_valid(new_state):
                successors.append(new_state)
    else:
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for move in moves:
            new_state = (M1 + move[0], C1 + move[1], 1, M2 - move[0], C2 - move[1])
            if is_valid(new_state):
                successors.append(new_state)
    return successors

def solve():
    initial_state = (3, 3, 1, 0, 0)
    goal_state = (0, 0, 0, 3, 3)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        if state == goal_state:
            return path + [state]

        for successor in get_successors(state):
            queue.append((successor, path + [state]))

    return None

solution = solve()

if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")
