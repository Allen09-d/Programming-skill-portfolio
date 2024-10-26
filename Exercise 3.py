'''
Exercise 3: Biography
'''

#This program collects personal information

#Make a variable then get user name, hometown, age
name=input("Enter your name: ")
hometown=input("Enter your hometown: ")
age=int(input("Enter your age: "))
print=(name,hometown,age)

#Create a dictionary to store all the information
my_info={
    "name":name,
    "hometown":hometown,
    "age":age}

#Print all the information stored in dictionary
#The f letter put dictionary values inside{}
print=(f"Name:{my_info['name']}\nHometown:{my_info['hometown']}\nAge: {my_info['age']}")




