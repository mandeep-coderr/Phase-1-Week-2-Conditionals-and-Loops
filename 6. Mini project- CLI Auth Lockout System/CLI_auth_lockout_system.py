correct_pin = "1234"
max_attempts = 3
is_locked = False

while max_attempts > 0:
    user_guess = input("Enter your PIN: ")
    if user_guess == "":
        print("You did not Type anything, Please enter your PIN ")

    elif user_guess == correct_pin:
        print("`Access Granted`")
        break

    else:
        max_attempts = max_attempts - 1
        print("Incorrect PIN")

        if max_attempts == 0:
            is_locked = True
            break

        else:
            print(f"You have {max_attempts} attempts left ")

if max_attempts == 0:
    print("Your ATM Card is blocked")            









    


