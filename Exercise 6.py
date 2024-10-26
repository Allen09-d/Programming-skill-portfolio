'''
Exercise 6: Brute Force Attack
'''

# Make the user to get the correct password
correct_password = "0000"

# Make the user to enter the password
while True:
    entered_password = input("Enter the password: ")
    
    # Check if the entered password is correct
    if entered_password == correct_password:
        print("Permission granted.")
        break  # Exit the loop if the password is correct
    else:
        print("Incorrect password. Try again.")
