# print(len("Adam"))

# print("Hello"[0])

text = "we are learning Python programming."

# Python String upper() Method
# Definition: This Method turns each character to UPPER case.
print (text.upper())
# Outcome - WE ARE LEARNING PYTHON PROGRAMMING.

# Python String lower() Method
# Definition: This Method turns each character to lower case.
print (text.lower())
# Outcome - we are learning python programming.

# Python String capitalize() Method
# Definition: This Method turns the first character to UPPER case.
print (text.capitalize())
# Outcome - We are learning python programming.

# Python String count() Method
# Definition: This Method counts how many times a character or phrase appears in the text.
print (text.count("p"))
# Outcome - 1 (This shows how many times the letter "p" appears in the text.  It is once, as this is case sensitive so the capital P is not counted)

# Python String find() Method
# Definition: This Method finds the specified word and tells you where it appears in the text.
print (text.find("learning"))
# Outcome - 7 (The word "learning" begins on character 7 in the text phrase)

# Python String replace() Method
# Definition: This Method finds a pre-defined word or phrase and replaces it with a different pre-defined work or phrase.
print (text.replace("we are", "I am"))
# Outcome - I am learning python programming.

# Python String strip() Method
# Definition: This Method removes specified characters from the start or end of the text.
print (text.strip("."))
# Outcome - we are learning python programming (In this case, it removes the . from the end of the sentence)
