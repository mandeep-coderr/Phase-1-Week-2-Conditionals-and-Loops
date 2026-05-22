# for loop
cars = ["Ford" , "Toyota" , "Honda"]
for car in cars:                     # for- A for loop is a tool that grabs items from a box (like a list) one by one, 
    print(car)                          # and repeats an action on each item until the box is empty

#range(stop) , range(start , stop) , range(start , stop , step)
for number in range(5):
    print(number)                    # stop

for number in range(2, 6):           # start / stop
    print(number)    

for number in range(2, 10, 2):       # start / stop / step
    print(number)    

#range() - count backwards
for number in range(10, 0, -1):      # range - count backwards
    print(number)    

# Looping over a string - each character one at a time  
secret_code = "A1B2"
for char in secret_code:             # Looping over a string- use for only one word
    print(char)

# enumerate() get both index and value
guests = ["Alice", "Bob" "Emma", "Noah", "Olivia", "Liam", "Ava", "Sophia", "Ethan", "Mia", "Jacob", "Isabella"]

for seat_number, guest in enumerate(guests):
    print(seat_number, guest)    

scores = ["999", "850"]                 # enumerate
for rank , score in enumerate(scores):
    print(rank , score)     

# for else - else runs when loop finishes without break
hallway = ["empty", "empty", "thief"]

for room in hallway:
    print("Checking room...")
    
    if room == "thief":
        print("Thief found! Pressing break button.")           # for else
        break
        
else:
    print("Radio Report: All rooms checked safely. No thief.")    


# for loop: The factory worker grabbing one item at a time.

# range(): The digital ticket dispenser generating numbers.

# String loops: Sliding your hand down a beaded necklace.

# enumerate(): The movie theater giving you both the Seat Number and the Guest.

# for-else: The security guard making a final radio report only if the break button 
# is never pressed.