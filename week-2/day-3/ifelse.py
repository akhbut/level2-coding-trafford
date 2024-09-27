# Example from Powerpoint
music = "classical"

if music == "classical":
    print("Oh no it's that classical again")
elif music == "no music":
    print("Arh, peace and quiet")
else:
    print("Nice and noisy")

# Activity 1

age = "18"

print("Hi - please may I have a pint of Cider?")

if age >= "18":
    print("Certainly!")
else:
    print("Sorry - you need to be over 18 years old")


# "And" Operator Example
place = "MCR"
weather = "Cloudy"

if place == "MCR" and weather == "Sunny":
    print("Check again")
elif place == "MCR" and weather == "Rain":
    print("Obvs")
else:
    print("What, it isn't raining?")

# Activity 2 - AND

age = "21"
country = "USA"

print("Hi - please may I have a pint of Cider?")

if age >= "21" and country.lower() == "usa":
    print("What's Cider?  How about Budweiser? Sure thing, buddy.  Have a nice day!")
elif age >= "21" and country.lower() != "usa":
    print("Where are you from?")
else:
    print("Sorry - you're not old enough")

# OR Methods Example

day = "Saturday"

if day.lower() == "Saturday" or day.lower() == "Sunday":
    print("It's the weekend!")
else:
    print("When's the weekend?")


# Truthy and Falsey

print("What is your name?")

name = input()

if name:
    print(f"Hello {name}, how are you?")
else:
    print("You did not give me your name!")