# If Else - Challenge 1

password = "password1"

if len(password) < 8:
    print("The password is too short.")
else:
    print("The password is:", password)


# If Else Challenge 2

num = 15

if num % 3 == 0 or num % 5 == 0:
    print("This number is divisible by 3 or 5.")
else:
    print("This number is not divisible by 3 or 5.")


# If Else Challenge 3

num = 21

if num % 3 == 0 and num % 7 == 0:
    print("fizz buzz")
elif num % 3 == 0:
    print("fizz")
elif num % 7 == 0:
    print("buzz")
else:
    print(num)


# If Else Challenge 4

word = "abba"

if word[0] == word[-1]:
    print(True)
else:
    print(False)


# If Else Challenge 5

time = 8
place_of_work = "Code Nation"
town_of_home = "Manchester"
 
if time < 8:
    print("They are at home")
elif time == 8:
    print("They are commuting")
elif time > 8 and time <= 17:
    print("They are at work")
elif time > 17:
    print("They are at home")
else:
    print("Who knows where they are?")


# If Else Challenge 6

num1 = 4
num2 = 6

sum_total = num1 + num2

if sum_total % 2 == 0:
    print("Success: The total sum is even.")
else:
    print("Unsuccessful: The total sum is odd.")


# If Else Challenge 7

# Need Help - Ahmar's solution below

# num = 12345

# string = str(num)

# if string[0] == string[-1] and string[1] == string[-2]:
#     print:(f"{num} is a palindrome")
# else:
#     print:(f"{num} is not a palindrome")

# Edmund's Solution

num_1b = 12345
rev_string_num_1b = int(str(num_1b)[::-1])

if rev_string_num_1b == num_1b:
    print("It is a palindrome")
else:
    print("It isn't a palindrome")


# If Else Challenge 8

# Need Help - Ahmar's solution below

text = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxchgfdjhiopiwquhejkdsoiufghedjwshi"

last_a_position = text.rfind("a")
last_e_position = text.rfind("e")
last_i_position = text.rfind("i")
last_o_position = text.rfind("o")
last_u_position = text.rfind("u")

last_vowel_position = max(last_a_position,last_e_position,last_i_position,last_o_position,last_u_position)
print(last_vowel_position)

