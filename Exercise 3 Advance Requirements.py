'''
Exercise 3: Biography
Advanced Requirements
'''

##This program collects personal information

#Make a variable then get user name, hometown, age
name=input("Enter your name: ")
hometown=input("Enter your hometown: ")

#This loop makes the user enter a valid number for age
while True:
    try: #Try function use to convert what the user types into a number
        age=int(input("Enter your age: "))
    except ValueError: #If it works, exit the loop break
      print("Please enter a valid number.")
        

#Create a dictionary to store all the information
my_info={
    "name": name,
    "hometown": hometown,
    "age": age
}

#Print all the information stored in dictionary
#The f letter put dictionary values inside{}
print=(f"Name: {my_info['name']}\nHometown: {my_info['hometown']}\nAge: {my_info['age']}")

