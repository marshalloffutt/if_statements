car = 'toyota'
print("Is car == 'toyota? I predict True.")
print(car == 'toyota')

print("\nIs car == 'audi? I predict False.")
print(car == 'audi')

food = 'banana'
print("\nIs food == 'banana? I predict True.")
print(food == 'banana')

print("\nIs food == 'pizza? I predict False.")
print(food == 'pizza')

friend = 'Larry'
if friend.lower() == 'larry':
    print(friend + " is your friend!")

print("\nIs Larry your friend?")
print(friend.lower() == 'larry')

larry = 33
gary = 34

if larry > 21 and gary > 21:
    print("Party time")

dudes = ['Larry', 'Barry', 'Jerry', 'Gary']

person = 'Terry'

if person not in dudes:
    print(person.title() + ", you are not one of my dudes.")
    dudes.append(person)

if person in dudes:
    print(person.title() + ", you are one of my dudes!")

