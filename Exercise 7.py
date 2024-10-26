'''
Exercise 7: Some counting
'''

#Loop that counts up to 0 to 50 in increments of 1
print("First loop - counting up from 0-50: ")
for number in range (0,51):
    print(number)

#Loop that counts down from 50 to 0 in decrements of 1
print("\nSecond loop - Counting down from 50 to 0: ")
for number in range(50, -1, -1):
    print(number)
    
#Loop that counts up to 30 to 50 in increments of 1
print("Third loop - counting up from 30-50: ")
for number in range (30,51):
    print(number)

#Loop that counts down from 50 to 10 in decrements of 2
print("\nFourth loop - Counting down from 50 to 10:")
for number in range(50, 9, -2):
    print(number)
    
#Loop that counts up from 100 to 200 in increments of 5
print("\nFifth loop - Counting up from 100 to 200:")
for number in range(100, 201, 5):
    print(number)