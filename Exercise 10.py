'''
Exercise 10: Is it even?
'''

def check_number(num):
    if num %2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
    
def main():
    print("Welcome to Even or Odd Checker!")
    number=int(input("Please enter a number: "))
    result=check_number(number)
    print(result)
main()


    

