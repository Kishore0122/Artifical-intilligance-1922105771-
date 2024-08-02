import itertools

def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to the starting city
    return total_distance

def tsp_brute_force(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    min_distance = float('inf')
    best_route = None
    
    for permutation in itertools.permutations(cities):
        current_distance = calculate_total_distance(permutation, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = permutation
    
    return best_route, min_distance

# Example usage
if __name__ == "__main__":
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    best_route, min_distance = tsp_brute_force(distance_matrix)
    print(f"Best Route: {best_route}")
    print(f"Minimum Distance: {min_distance}")
