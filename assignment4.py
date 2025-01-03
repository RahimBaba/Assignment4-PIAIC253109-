#Python List Exercises

#Exercise 3-1: Names
print("\n Exercise 3-1: Names")
names = ["Ahsan", "Ahmad", "Omer", "Ali"] # List of friends names
# Print each name by accessing each element in the list
for name in names:
    print(name)

#Exercise 3-2: Greetings
print("\n Exercise 3-2: Greetings")
for name in names:  # Print a personalized message for each person
    print(f"Hello, {name}! Welcome to the Python Course!")

#Exercise 3-3: Your Own List
print("\n Exercise 3-3: Your Own List")
transportation = ["BMW1000RR", "Ducati", "kawasaki Ninja H2R", "Boeing private jet"]
# Print a series of statements about these items
for item in transportation:
    print(f"I would like to own a {item}.")

#Exercise 3-4: Guest List
print("\n Exercise 3-4: Guest List")
dinner_guests = ["Farooq", "Hamza", "Taha"]
for guest in dinner_guests:   # Print a personalized invitation for each guest
    print(f"Dear {guest}, I would be honored to have you join me for dinner!")

#Exercise 3-5: Changing Guest List
print("\n Exercise 3-5: Changing Guest List")
unable_to_attend = "Taha"   # Inform about the guest who can't make it
print(f"Unfortunately, {unable_to_attend} can't make it to the dinner.")

# Replace the guest who can't make it with a new guest
dinner_guests[dinner_guests.index(unable_to_attend)] = "Hannan"

# Print the updated set of invitation messages
for guest in dinner_guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner!")


#Exercise 3-6: More Guests
print("\n Exercise 3-6: More Guests")
print("Good news! I found a bigger dinner table, so I can invite more people!")   # Inform everyone about the bigger table
dinner_guests.insert(0, "Akbar")  # Add one guest to the beginning of the list
middle_index = len(dinner_guests) // 2   # Add one guest to the middle of the list
dinner_guests.insert(middle_index, "Zubair")
dinner_guests.append("Ali Hamza")   # Add one guest to the end of the list
for guest in dinner_guests:   # Print the updated set of invitation messages
    print(f"Dear {guest}, I would be honored to have you join me for dinner!")


#Exercise 3-7: Shrinking Guest List
print("\n Exercise 3-7: Shrinking Guest List")
print("Unfortunately, my new dinner table won’t arrive in time, so I can only invite two people for dinner.")   # Inform everyone about the reduced guest list
# Remove guests until only two remain, apologizing to each removed guest
while len(dinner_guests) > 2:
    removed_guest = dinner_guests.pop()
    print(f"Sorry, {removed_guest}, but I can't invite you to dinner this time.")

for guest in dinner_guests:   # Inform the remaining two guests they are still invited
    print(f"Dear {guest}, you’re still invited to dinner!")

# Remove the last two guests using del and confirm the list is empty
del dinner_guests[0]
del dinner_guests[0]

print(f"My guest list is now empty: {dinner_guests}")    # Print the empty list



#Exercise 3-8: Seeing the World
print("\n Exercise 3-8: Seeing the World")
# List of places I'd like to visit
places = ["Kyoto", "Santorini", "Machu Picchu", "Banff", "Cairo"]

print("Original list:")   # Print the original list
print(places)

print("\nList in alphabetical order:")  # Print the list in alphabetical order without modifying it
print(sorted(places))

print("\nOriginal list after sorted():")   # Show the list is still in its original order
print(places)

print("\nList in reverse-alphabetical order:")  # Print the list in reverse-alphabetical order without modifying it
print(sorted(places, reverse=True))

print("\nOriginal list after sorted() with reverse=True:")   # Show the list is still in its original order
print(places)

places.reverse()   # Use reverse() to change the order of the list
print("\nList after reverse():")
print(places)

places.reverse()   # Use reverse() again to change the list back to its original order
print("\nList after reversing again:")
print(places)

places.sort()    # Use sort() to change the list to alphabetical order
print("\nList after sort() in alphabetical order:")
print(places)

places.sort(reverse=True)    # Use sort() to change the list to reverse-alphabetical order
print("\nList after sort() in reverse-alphabetical order:")
print(places)


#Exercise 3-9: Dinner Guests
print("\n Exercise 3-9: Dinner Guests")

print("Unfortunately, my new dinner table won’t arrive in time, so I can only invite two people for dinner.")   # Inform everyone about the reduced guest list

while len(dinner_guests) > 2:   # Remove guests until only two remain
    removed_guest = dinner_guests.pop()
    print(f"Sorry, {removed_guest}, but I can't invite you to dinner this time.")


for guest in dinner_guests:    # Inform the remaining two guests they are still invited
    print(f"Dear {guest}, you’re still invited to dinner!")

print(f"\nI am now inviting {len(dinner_guests)} people to dinner.")   # Print the number of people being invited to dinner



#Exercise 3-10: Every Function
print("\n Exercise 3-10: Every Function")
# Create a list of mountains
mountains = ["Everest", "K2", "Tirch Mir", "Naga Parbat", "Broad Peak"]

print("Original list of mountains:")  # Print the original list
print(mountains)

print("\nThe first mountain in the list is:")  # Accessing individual elements
print(mountains[0])

mountains[2] = "Elbrus"   # Modifying an element in the list
print("\nList after modifying the third mountain:")
print(mountains)

mountains.append("Matterhorn")   # Adding a new element to the end of the list
print("\nList after adding a new mountain:")
print(mountains)

mountains.insert(2, "Tirch Mir")    # Inserting an element into a specific position
print("\nList after inserting 'Tirch Mir' back into the third position:")
print(mountains)

del mountains[3]    # Removing an element using del
print("\nList after deleting the fourth mountain:")
print(mountains)

popped_mountain = mountains.pop()   # Removing an item using pop()
print(f"\nRemoved mountain using pop(): {popped_mountain}")
print("List after popping an element:")
print(mountains)

mountains.remove("K2")   # Removing an item by value
print("\nList after removing 'K2':")
print(mountains)

mountains.sort()   # Sorting the list permanently
print("\nList after permanent sorting:")
print(mountains)

mountains.sort(reverse=True)    # Sorting the list in reverse-alphabetical order permanently
print("\nList after permanent reverse sorting:")
print(mountains)

print("\nTemporarily sorted list:")   # Temporarily sorting the list
print(sorted(mountains))

print("\nOriginal list after temporary sorting:")    # Show that the original list remains unchanged
print(mountains)

mountains.reverse()    # Reversing the order of the list
print("\nList after reversing the order:")
print(mountains)

# Finding the length of the list
print(f"\nThe number of mountains in the list is: {len(mountains)}")



#Exercise 3-11: Intentional Error
print("\n Exercise 3-11: Intentional Error")
# Create a list of mountains
mountains = ["Everest", "K2", "Tirch Mir", "Naga Parbat", "Broad Peak"]

# Intentional IndexError: Trying to access an index that doesn't exist
print("\nTrying to access an out-of-range index:")
try:
    print(mountains[10])  # This index does not exist
except IndexError:
    print("IndexError: Trying to access an index that is out of range!")

# Correcting the error by using a valid index
print("\nAccessing a valid index (index 2):")
print(mountains[2])  # 'Trich Mir' is at index 2


