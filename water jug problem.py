from collections import deque
def is_solvable(jug1_capacity, jug2_capacity, target):
    if target > max(jug1_capacity, jug2_capacity):
        return False
    if target % gcd(jug1_capacity, jug2_capacity) != 0:
        return False
    return True
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def water_jug_solver(jug1_capacity, jug2_capacity, target):
    if not is_solvable(jug1_capacity, jug2_capacity, target):
        print("No solution exists")
        return False
    visited = set()
    queue = deque([(0, 0)])
    steps = []
    while queue:
        jug1, jug2 = queue.popleft()
        steps.append((jug1, jug2))
        if jug1 == target or jug2 == target or jug1 + jug2 == target:
            print("Steps to achieve the target:")
            for step in steps:
                print(step)
            return True
        possible_states = [
            (jug1_capacity, jug2),
            (jug1, jug2_capacity),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)),
        ]
        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    print("No solution exists")
    return False
jug1_capacity = 4
jug2_capacity = 3
target = 2
water_jug_solver(jug1_capacity, jug2_capacity, target)
