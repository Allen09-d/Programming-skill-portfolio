'''
Exercise 6: Brute Force Attack
Advanced Requirements
'''

# Make the user to get the correct password
correct_password = "0000"
max_attempts=5 #Maximum number of allowed attempts
attempts=0#Number of attempts encountered

#Keep asking for passwords
while attempts<max_attempts:
    #Get password from user
    password=input("\nEnter password: ")
    
    #increment attempt counter
    attempts +=1
    
    #Check if password is correct
    if password == correct_password:
        print("Permission granted! Welcome to the system.")
        break #Exit the loop if the password is correct
    else:
        #Check the remaining attempts
        remaining=max_attempts - attempts
        
        if remaining >0:
            #Tell user the password incorrect and the remaining attempts
            print("\nIncorrect password.")
            print(f"\nYou have {remaining} attempts remaining.")
        else:
                print("\nMaximum attempts reached.")
                print("System locked.")
        #If they go out with loop by getting the password right       
        if password == correct_password:
            print("You may now proceed with your tasks.")
                
                
                

