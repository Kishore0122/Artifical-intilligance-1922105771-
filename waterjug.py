def water_jug_problem(jug1_capacity, jug2_capacity, target):
    jug1, jug2 = 0, 0

    while jug1 != target and jug2 != target:
        if jug1 == 0:  
            jug1 = jug1_capacity
        elif jug2 == jug2_capacity:  
            jug2 = 0
        else:  
            pour_amount = min(jug1, jug2_capacity - jug2)
            jug1 -= pour_amount
            jug2 += pour_amount

        print(f"Jug1: {jug1}/{jug1_capacity}, Jug2: {jug2}/{jug2_capacity}")


jug1_capacity = int(input("Enter the capacity of jug 1: "))
jug2_capacity = int(input("Enter the capacity of jug 2: "))
target = int(input("Enter the target amount of water: "))

water_jug_problem(jug1_capacity, jug2_capacity, target)