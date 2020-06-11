#Write a program that returns every other char of a given string starting with first using a function named “string_alternative”
#Str = “Good evening”
#Output: Go vnn
#Note: You need to create a function named “string_alternative” for this program and call it from main function.


def string_alternative(str):
    return str[::2]

myStr = input("\nPlease provide a string: ")
print("Here is your alternate string: ",string_alternative(myStr))
