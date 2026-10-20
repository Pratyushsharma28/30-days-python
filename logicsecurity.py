username = "admin"
password = "1234"
otp = "5678"
active = True
attempts = 0

while attempts < 3:
    user = input("Enter username:")
    pass_word = input("Enter password")
    if user == username:
        if pass_word == password:
            if active:
                enter_otp = input("Enter otp")
                
                if enter_otp == otp:
                    print("Logic successfull")
                    break
                else:
                    print("Invalid otp")
            else:
                print("account is inactive")
        else:
            print("Incorrect password")
    else:
        print("Incorrect username")
    attempts = attempts + 1
    if attempts == 3:
        print("Account locked")