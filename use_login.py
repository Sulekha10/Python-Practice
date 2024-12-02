# use login system

# predefined username and password
stored_username = "admin"
stored_password = "password123"

# Take user input
username = input("Enter username : ")
password = input("Enter password : ")

# check login credentials
if username == stored_username:
    if password == stored_password:
        print('Login successful!')
    else:
        print("Incorrect password")
else:
    print("username not found.")

