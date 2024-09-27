# # Functions Example

# def press_grind_beans():
#     print("Grinding for 20 seconds")

# press_grind_beans()





# # Parameters Example

# def cash_withdrawal(amount, accnum):
#     print(f"Withdrawing £{amount} from account {accnum}.")

# cash_withdrawal(300, 50449921)
# cash_withdrawal(30, 50449921)
# cash_withdrawal(200, 50449921)




# # Activity 3

# def coffee_order(size, milk_type, drink_type):
#     print(f"Your {size} {milk_type} milk {drink_type} is being made.")

# coffee_order("large", "oat", "latte")





# # Further Parameters Example

# w_amount = 100
# account_num = 12345678

# def cash_withdrawal(amount, accnum):
#     print(f"Withdrawing £{amount} from account {accnum}.")

# cash_withdrawal (w_amount, account_num)




# # Challenge 1

# order_count = 0

# def take_order(size, topping):
#     global order_count
#     print(f"{size} Pizza with {topping}.")
#     order_count +=1

# take_order("Large", "Ham & Pineapple")
# take_order("Medium", "Pepperoni")
# take_order("Large", "Nduja Sausage & Peppers")


# print(f"There are {order_count} orders in total.")




# # Challenge 2

# print("Welcome to the Barclays Bank Cash Machine")

# def cash_machine_withdrawal(pin, amount):
#     correct_pin = 1234
#     account_balance = 1000

#     if pin == correct_pin:
#         if amount <= account_balance:
#             account_balance -= amount
#             print("Dispensing Cash")
#             print(f"New Bank Balance: £{account_balance}")
#         else: print("Insuffient Funds Available")
#     else: print("Incorrect PIN")
    
# user_pin = int(input("Please enter your PIN: "))
# withdraw_amount = int(input("Please enter the amount you'd like to withdraw: "))

# cash_machine_withdrawal(user_pin, withdraw_amount)



# # Extra Reading - Return

# def add_up(num1, num2):
#     return num1 + num2

# # This adds up the two numbers and returns it, but without printing it
# add_up(7,3)

# # This adds up the two numbers, returns it and prints it
# print(add_up(2, 5))


# # Extra Reading - Returns ++

# current_temp_c = 19

# def multiply_by_nine_fifths(celcius):
#     return celcius * (9/5)

# def get_fahrenheit(celcius):
#     return multiply_by_nine_fifths(celcius) + 32

# print(f"The temperature is {get_fahrenheit(current_temp_c)}°F.")



# # Extra Reading: Global & Local Variables

# coffee_is_grinding = False

# def press_grind_beans():
#     global coffee_is_grinding
#     if coffee_is_grinding:
#         print("Stopping the grind")
#         coffee_is_grinding = False
#     else:
#         print("Grinding is about to begin")
#         coffee_is_grinding = True

# press_grind_beans()
# press_grind_beans()