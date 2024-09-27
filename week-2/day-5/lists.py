# # Acitivity 1
 
# def multiply(num1, num2):
#     return num1 * num2

# print(multiply(2, 5))

# # Lists Example

# coffee_order = [
#     "Alex - Cortado",
#     "Ben - Latte",
#     "Charlie - Whatever's new"
# ]

# print(coffee_order)


# # Activity 2

# favourite_songs = [
#     "Robyn - Be Mine",
#     "Imogen Heap - The Walk",
#     "Britney Spears - (You Drive Me) Crazy [Stop Remix]"
# ]

# print(favourite_songs)


# # Activity 2 - Further Lists Example

# favourite_songs = [
#     "Robyn - Be Mine",
#     "Imogen Heap - The Walk",
#     "Britney Spears - (You Drive Me) Crazy [Stop Remix]"
# ]

# print(favourite_songs[1])

# # The Inclusion of [1] means it'll only print the 2nd item in the list (as python starts counting at 0)


# # Further Example of Lists - Changing an Item

# coffee_order = [
#     "Alex - Cortado",
#     "Ben - Latte",
#     "Charlie - Whatever's new"
# ]

# coffee_order[1] = "Ann - Vanilla latte"

# print(coffee_order)



# # Further Example of Lists - Length of List - How many items are on the list

# coffee_order = [
#     "Alex - Cortado",
#     "Ben - Latte",
#     "Charlie - Whatever's new"
# ]

# print(len(coffee_order))


# # Further Example of Lists - Add an item to the end of the list (Append)

# coffee_order = [
#     "Alex - Cortado",
#     "Ben - Latte",
#     "Charlie - Whatever's new"
# ]

# coffee_order.append("Sabrina - Espresso")

# print(coffee_order)



# # Further Example of Lists - Remove the item from the end of the list (Pop)

# coffee_order = [
#     "Alex - Cortado",
#     "Ben - Latte",
#     "Charlie - Whatever's new"
# ]

# coffee_order.append("Sabrina - Espresso")

# print(coffee_order)

# coffee_order.pop()

# print(coffee_order)


# # Sort() Example

# singers = [
#     'Lady Gaga',
#     'Celine Dion',
#     'Whitney Houston',
#     'Mariah Carey',
#     'Britney Spears',
#     'Christina Aguilera'
#     ]
 
# singers.sort()
 
# print(singers)
 
# # output: ['Britney Spears', 'Celine Dion', 'Christina Aguilera', 'Lady Gaga', 'Mariah Carey', 'Whitney Houston']








# Python List Activities - Extra Work

# # 1) Write a python program to sum all the items in a list.  
# numbers_list = [1, 2, 3, 4, 5]
# total_sum = sum(numbers_list)
# print("Sum of the list:", total_sum)


# # 2) Write a python program to multiply all the items in a list.  
# numbers_list = [1, 2, 3, 4, 5]
# result = 1
# for number in numbers_list:
#     result *= number
# print("Product of the list:", result)


# # 3) Write a python program to get the largest number from a list. 
# numbers_list = [1, 2, 3, 4, 5]
# largest_number = max(numbers_list)
# print("Largest number in the list:", largest_number)


# # 4) Write a python program to count the number of strings from a given list of strings where the string length is 2 or more and the first and last characters are the same.  
# favourite_phrases = ["hello", "tricky", "abc", "abba", "1221"]
# count = 0
# for string in favourite_phrases:
#     if len(string) >= 2 and string[0] == string[-1]:
#         count += 1
# print("Count of specified strings:", count)


# 5) Write a python program to remove duplicates from a list.

