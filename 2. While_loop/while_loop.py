# pushups = 0

# while pushups < 3:
#     print("Doing a pushup!")                                  #
#     pushups = pushups + 1

# TOPIC 1: The Loop Variable (The Box)
items_packed = 0  

 # TOPIC 2: The While Loop 
while items_packed < 3:  
    print("Packing an item into the box...")
    
    items_packed = items_packed + 1  

print("All items packed! Ready for delivery.")    

#combined loop variable + while loop
rocket_timer = 10

while rocket_timer > 0:
    print(rocket_timer)
    rocket_timer = rocket_timer - 1

print("Rocket_launched")

#break
search_number = 1

while search_number <= 5:
    if search_number == 4:
        break
        
    print(search_number)
    search_number = search_number + 1

print("Search over.")