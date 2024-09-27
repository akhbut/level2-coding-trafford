# favourite_drinks = ["coke", "fanta", "tonic"]

# for drink in favourite_drinks:
# 	print(drink)
	




# # To Slow Down the Process of printing the list
# from time import sleep

# favourite_drinks = ["coke", "fanta", "tonic"]

# for drink in favourite_drinks:
# 	sleep(0.5)
# 	print(drink)




# # To Print a Range - values: (starting position, stopping position, number of steps)

# for i in range(0, 10, 2):
#     print(i)



# # Activity 1

# favorite_films = ["West Side Story", "Ghostbusters", "Interstellar", "Mean Girls"]

# for film in favorite_films:
#     print(film)

# def film_check(films):
#     if "Ghostbusters" in films:
#         print("Yay Ghostbusters")
#     else:
#         print("Boo, no Ghostbusters?")

# film_check(favorite_films)



# # Activity 2

# for i in range(9, -1, -1):
#     print(i)


# # While Loops

# num = 0

# while num < 10:
#     num +=1
#     print(num)




# # While Loops Example - Random Number Generator with Counter

# from random import randint

# target_number = 79

# generated_number = randint(1,100)
# counter = 0

# while generated_number != target_number:
#     print(counter, generated_number)
#     generated_number = randint(1,100)
#     counter += 1

# print(f"You found the number!  It was number {generated_number}, and you found it in {counter} guesses.")



# # Challenge 1

# # for loop

# for i in range(0,13):
#     print("hello world")

# # while loop

# count = 0
# while count < 13:
#     print("hello world")
#     count += 1






# # # Challenge 2

# from random import randint

# for i in range(0,6):
#     num = randint(1, 30)
#     if num % 7 == 0:
#         print(f"{num} is divisible by 7")
#     else:
#         print(f"{num} is not divisible by 7")



# Challenge 3

# import random

# cards = ["Diamond", "Spade", "Club", "Heart"]
# target_suit = "Heart"
# current_card = ""

# while current_card != target_suit:
#     current_card = random.choice(cards)
#     print(f"Current card: {current_card}")

# print(f"Found the target suit: {target_suit}")


# # Challege 4 - Times Table Generator

# times_table = int(input("Please enter the times tables you want to see, or 13 and above to exit> "))
# while times_table != 13:
#     for index in range(1,13):
#         result = index * times_table
#         print(f"{index} x {times_table} = {result}")
#     times_table = int(input("Please enter the times tables you want to see, or 13 and above to exit> "))

# Challenge 5 - Create a program that checks whether all numbers between 1 and 20 are prime numbers or not


# # Joseph's Answer

# z = 0
 
# for x in range (1,21):
#     for y in range(1,21):
#         if x % y != 0:
#             z += 1
#     if z >= 18 and x != 1:
#         print(f"{x} is a prime number")
#     z = 0

# Mark's Answer:

list_of_primes = [2]

target_number = int(input("Please enter the maximum number you want to find a list of prime numbers: "))

for x in range (3, target_number, 2):
    x_is_prime = True
    for y in list_of_primes:
        if x%y == 0:
            x_is_prime = False
    if x_is_prime == True:
        list_of_primes.append(x)

for prime in list_of_primes:
    print(prime)

