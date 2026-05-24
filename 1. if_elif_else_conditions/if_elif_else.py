# # if statement
# age = 25
# if age >= 18:
#     print("You can enter the club.")           # if

# # else statement
# age = 15
# if age >= 18:
#     print("You can enter the club.")
# else:                                          # else
#     print("Sorry, you are too young.")    

# # # if / else statement
# temperature = 20
# if temperature >= 25 :
#     print("It is hot")                         # if / else
# else:
#     print("It is cold")

# # # if / elif / else
# total_score = 75
# if total_score >= 90:
#     print("Grade A")                          # if / elif / else
# elif total_score >= 70:
#     print("Grade B")
# else:
#     print("Grade C")        

# # #indentation
# age = 19
# if age >= 18:
#     print("Welcome new adults") 


        # New Part start with Socratic Teacher / Senior Python Mentor 

player_key = "golden"

if player_key == "golden":                    # if condition
    print("The treasure chest opens!")

# Else Condition
entered_password = "Batman"
if entered_password == "superman":
    print("Vault unlocked!")

else:
    print("Intruder alert!") 

# if / else / elif
order_status = "shipped"
if order_status == "packing":
    print("We are putting your items in the box.")
elif order_status == "shipped":
    print("Your order is on the way! ")
elif order_status == "delivered":
    print("Your package has arrived at your door! ")
else:
    print("Let us check with the warehouse.") 

# Nested if- outer if within others if in inner boxes- if inside an if
castle_key = "yes"
sword = "yes"
magic_shield = "yes"

if castle_key == "yes":
    print("You unlocked the castle.")
    if sword == "yes":
        print("You bravely enter the boss room.")
        if magic_shield == "yes":
            print("You defeated the dragon!")
        else:
            print("The dragon burned you! ") 
    else:
        print("You run away from the guards. ")        

else:
    print("The door is locked ") 

# Ternary expression - new way to use if else in short code       
guest_status = "VIP"

entry_fee = 150 if guest_status == "VIP" else 300

print(entry_fee)



# FREE User / Pro User

# Backend
user_subscription = "inactive"
# active/inactive

# main work

# active == active -> true
# active == inactive -> false
# 3 == 5 -> false

user_Label = "Free"
if user_subscription == "active":
    user_Label = "Pro"
else:
    user_Label = "Free"

print("User:", user_Label)

user_subscription = "inactive"
user_Label = "Pro" if user_subscription == "active" else "Free"
