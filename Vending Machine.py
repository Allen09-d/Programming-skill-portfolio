'''
Making a Vending Machine
'''


vending_menu = ["Drinks", "Chips"]
drinks_dict = {
    1:{'Soda': 'Mountain Dew', 'price': 3.00},
    2:{'Soda': 'Coca-Cola', 'price': 3.00},
    3:{'Soda': 'Fanta', 'price': 3.00},
    4:{'Soda': 'Pepsi', 'price': 3.00},
    5:{'Water': 'Mai Dubai', 'price': 1.00},
    6:{'Water': 'Pocari Sweat', 'price': 4.25},
    7:{'Energy Drink': 'Red Bull', 'price': 6.50}
    }
chips_dict = {
    1:{'Chips': 'Dorritos', 'price': 5.00},
    2:{'Chips': 'Lays Chips', 'price': 4.25},
    3:{'Chips': 'Cheetos', 'price': 4.25},
    4:{'Chips': 'Takis', 'price': 4.25},
    5:{'Chips': 'Piattos', 'price': 4.25},
    6:{'Chips': 'Nova', 'price': 4.25},
    7:{'Chips': 'Buggles', 'price': 3.00}
    }
sweets_dict = {
    1:{'Chocolate candy': 'M&Ms', 'price': 3.00},
    2:{'Chocolate bar': 'Snickers', 'price': 3.25},
    3:{'Chocolate bar': 'Reeses', 'price': 3.25},
    4:{'Chocolate bar': 'Twix', 'price': 3.00},
    5:{'Fruit candy': 'Skittles', 'price': 2.50},
    6:{'Chocolate bar': 'Kitkat', 'price': 3.00}
    }
total = 0

import pyttsx3 
import datetime

engine=pyttsx3.init('sapi5') #Using voice engine function
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour=int(datetime.datetime.now().hour) #Using datetime function to make realistic
    if hour>=0 and hour<=12:
        speak("Good morning")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Welcome to AJ's SnackStation where you can easily satisfy your cravings!")
    
speak("Hello there!")
wishme()

def vending_menu_func():
    print(vending_menu)
    x = str(input("\n\nChoose which category you want. Type FINISH to quit.\n\n"))
    if x == 'Drinks': #I use the if condition when the consumer chose drinks
        drinks_func()
    elif x == 'Chips': #I use the if condition when the consumer chose chips
        chips_func()
    else:
        print("\n\nHAVE YOUR CRAVINGS SATISFIED!\n")
        change_func() #It will print the receipt once the purchase is done

def sweets_func():
    global total
    print(sweets_dict)
    print("\n\nPlease choose what kind of sweets you want. If none, type FINISH to quit.\n") 
    sweets_input = input()  #Reading this input as a string
    if sweets_input.upper() == 'FINISH':  #I use uppercase method to compare as string
        vending_menu_func()
    else:
        sweets_id = int(sweets_input)  #This is to convert to an integer, if not 'FINISH'
        if sweets_id in sweets_dict:
            sweets_cost = sweets_dict[sweets_id]['price']
            total += sweets_cost
            vending_menu_func()
        else:
            print("\n\nPlease enter a valid order of sweets!\n")
            sweets_func() #The loop will continue to print unless the input is correct.

def drinks_func():
    global total
    print(drinks_dict)
    print("\n\nPLease choose what kind of drinks you want. If none, type FINISH:\n") 
    drink_input = input()  #Reading this input as a string
    if drink_input.upper() == 'FINISH':  #I use uppercase method to compare as string
        vending_menu_func()
    else:
        drink_id = int(drink_input)  #This is to convert to an integer, if not 'FINISH'
        if drink_id in drinks_dict:
            drink_cost = drinks_dict[drink_id]['price']
            total += drink_cost
            sweets_func()
        else:
            print("\n\nPlease enter a valid order of drinks!\n\n")
            drinks_func() #The loop will continue to print unless the input is correct.
            
def another_drink():
    x = input("\n\nWould you like to get another drink? Type YES or NO:\n")
    if x == 'YES': #I use the if condition to ask the buyer for another purchase 
        drinks_func()
    else:
        vending_menu_func() #After answering, it will return to main menu
            
def chips_func():
    global total
    print(chips_dict)
    print("\n\nPlease choose what kind of chips you want:\n") 
    chips_id = int(input()) #I use the integer to print the item id for chips
    if chips_id in chips_dict:
        chips_cost = chips_dict[chips_id] ['price']
        total += chips_cost #Will use the assignment operator to total the cost of the chips
        sweets_func()
    else:
        print("\n\nPlease enter a valid order of chips!\n\n")
        chips_func() #The loop will continue to print unless the input is correct.
        
def another_chips():
    x = input("\n\nWould you like to get another chips? Type YES or NO:\n")
    if x == 'YES': #I use the if condition to ask the buyer for another purchase 
        chips_func()
    else:
        vending_menu_func() #After answering, it will return to main menu

def change_func():
    global total
    print("\n\nTHANK YOU FOR BUYING. PLEASE COMEBACK LATER FOR MORE!")
    change = coins - total #Will use the arithmetic operators to subtract the total to the coins for the change
    print("\nPaid", coins, "with", str(total), ". And your change will be:", change)

print(" ̶ ̶ ̶»̶ ̶̶̶ ̶ »̶ Welcome to AJ's SnackStation Where You Can Easily Satisfy Your Cravings! «̶ ̶̶̶ ̶ «̶ ̶̶̶ ")
coins = float(input('\nPlease enter your coins:\n '))

coin_type = str(input('\n\nHello there! Are your coins DIRHAMS? Please enter YES or NO:\n'))
if coin_type == "YES": #If true continue with the next print
    print("\nYou have entered", str(coins), "DIRHAMS. Please select the category you want:\n")
    print(vending_menu)
    print("\n\nPlease enter the category you want:\n")
    category_selection = str(input()) #It will let the costumer to choose between drinks and chips in main menu 
    if category_selection == 'Drinks':
        drinks_func()
    elif category_selection == 'Chips':
        chips_func() #I use the if-elif condition for the main menu 
    else:
        print("Please try again.") #The loop will break once there is an error in the input
else:
    print('\nSorry! but we only accept Dirhams') #The loop will break once there is an error in the input

