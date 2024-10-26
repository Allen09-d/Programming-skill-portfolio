'''
Exercise 8: Simple Search
'''

#Make the list of names
names=["jake", "zac", "ian", "ron","sam","dave"]

#Show all names on the lists
print("\nHere are all the names in the list")
print(names)

#Ask user what name to search for
search_name=input("\nWhat name do you want to search for? ")

#Look for the name
if search_name in names:
    print(f"\nYes! I found {search_name} in the list.")
else:
    print(f"\nSorry, I couldn't find {search_name} in the list.")


