'''
Exercise 5: Days of the month
Advanced Requirements
'''

#Create a dictionary with months and days
days_in_month={
    1: 31, #January
    2: 28, #February (separately input the leap year)
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
month_names = {
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
 
while True:
    try:
        month=int(input("Enter a month number (1-12): ")) #Put a month number
        #Check if month is valid
        if month <1 or month >12:
            print("Enter a number between 1 to 12.")
            continue
        #Get the month name
        month_name=month_names[month]
        #Leap year for February
        if month == 2:
            while True:
                leap_year=input("Is this a leap year? (yes/no):").lower()
                if leap_year == "yes":
                    print("\nFebruary has 29 days in a leap year.")
                else:
                    print("\nFebruary has 28 days in a non-leap year.")
                    break
              
        #For all other months
                
        else:
                    days=days_in_month[month]
                    print(f"\n{month_name} has {days} days.")
                    print("Thank you for using Month/Days checker.")
                    break
    except ValueError:
     print("Please enter a valid number.")
                    
                    
                
                
                
                
                
                
        
        
            
        
