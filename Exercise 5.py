'''
Exercise 5: Days of month
'''

#Create a dictionary with months and days
days_in_month={
    1: 31, #January
    2: 28, #February 
    3: 31, #March
    4: 30, #April
    5: 31, #May
    6: 30, #June
    7: 31, #July 
    8: 31, #August
    9: 30, #September
    10: 31, #October
    11: 30, #November
    12: 31, #December
}

#Create a dictionary for the names of each month
months_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July", 
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

#Input the variables

try:
    month_number=int(input("Enter the month number (1-12): ")) #Ask the user input
    #Evaluate the answers
    if month_number in days_in_month:
        print(f"There are {days_in_month[month_number]} days in month {month_number}.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
except ValueError:
    print("Invalid input. Enter a valid month number.")

