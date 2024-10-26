'''
Exercise 4: Primitive Quiz
Advanced Requirements
'''

#Get the answer from the user 
answer=input("What is the capital of France? ")
#Check the answer using if and else function
if answer.lower() == "paris":
    print("Correct! Paris is the capital of France.")
else:
    print("Your answer is incorrect. The capital of France is Paris.")
    
#Multiple Questions

countries = {
    "France": "Paris",
    "Greece": "Athens",
    "Ireland": "Dublin",
    "Finland": "Helsinki",
    "Ukraine": "Kiev",
    "Portugal": "Lisbon",
    "Spain": "Madrid",
    "Norway": "Oslo",
    "Italy": "Rome",
    "Sweden": "Stockholm",
}

#loop through the list of countries
for country, capital in countries.items():
    answer=input(f"What is the capital of {country}? ").strip() #Ask a question about country's capital
    
    if answer.lower() == capital.lower(): #Check the program using if and else function
        print("Your answer is correct!")
    else:
        print(f"Incorrect! The capital of {country} is {capital}.\n")

print("Congrats! You finished the quiz.")
