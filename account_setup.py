print("---------------------------------")
print("rock paper scissors account setup")
print("---------------------------------")
while True:
    username = input("pick a username:  ")
    password = input("pick a password:  ")
    confirm_password = input(" confirm password: ")
    if password != confirm_password:
        print("password dont match try again")
    if  password == confirm_password:
        print("your account has been set up")
        text_file= open("account.csv","a")
        text_file.write(",")
        text_file.write(username)
        text_file.write(",")
        text_file.write(password)
        text_file.close
        break
    
