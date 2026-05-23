for sets in range(1 , 4):   
    for pushups in range(1 , 6):       
        print(f"set is {sets} pushup is {pushups}") 

#outer loop runs once - inner loop runs completely
for order in range(1 , 3):
    print(f"Starting Order{order}")

    for pizza in range(1 , 4):
        print(f"Baking Pizza{pizza}")

    print(f"Order{order} is out for delivery") 

#Time complexity intuition nested loop = n ** 2 iteration for n items - n stand for number of items

total_actions = 0
items = 10

for outer in range(items):
    for inner in range(items):
        total_actions = total_actions + 1

print(f"For {items} items, the computer did {total_actions} actions.")

# Break inside nested loop
for floor in range(1, 4):
    print(f"Arrived at Floor {floor}")
    
    for room in range(1, 5):
        if room == 3:
            print("  TIGER IN ROOM 3! BREAKING THE LOOP!")
            break
            
        print(f"  Checked Room {room} - All safe")

#Using nested loops for patterns (rows and columns)
for row in range(3):
    for column in range(5):
        print("*", end="")
    print()        




