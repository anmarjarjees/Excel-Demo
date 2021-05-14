# We are calling our module "my_modules" and using total function
from excel_functions import *

# now need to import from colorama:
# we imported a class named "Fore"
from colorama import Fore

# Part 1: ask the user to input their numbers:
# Colorama: Fore.LIGHTBLUE_EX`
numbers = input(Fore.LIGHTBLUE_EX +
                "Please enter your list of numbers as comma seperated values (csv): ")

# printing the values
# print(numbers) "90,92,88,84"

# printing the type
# print(type(numbers)) # <class 'str'>
# the input: "90, 92, 88, 82, 78, 94, 85"
# convert the input string to a list: ["90", "92", "88", "82", "78", "94", "85"]

# Step 1: We need to convert this string into a list ????
# str.split([chars]) => Return a list of the words in the string
# split() method will "return" a list
# Please be carfull that only one character has to be exist between each number which is the ","

numbers_list = numbers.split(",")
# test:
print(numbers_list)  # ['1', '2', '3', '4']

print(type(numbers_list))  # <class 'list'>

# below we are just printing the list of numbers for the user
# The syntax: for any_name in my_list_name
for item in numbers_list:
    print(item)

# Part 2: Ask the user about what formula (operation) they want to do with the list:
# 1 for total
# 2 for average (the mean)
# 3 for max
# 4 for min

# We need to give an initial value of formula in order to validate the while condition
formula = 0
while (formula != 5):
    print(" ***** Excel Formulas Game ***** ")
    print("1: Find the total")
    print("2: Find the average (the mean)")
    print("3: Find the maximum number")
    print("4: Find the minimum")
    print("5: Exit")

    # Don't forget that input() function returns a string data type (exactly like prompt function in JS)
    formula = int(input(Fore.LIGHTYELLOW_EX+"Please enter you choice: "))
    # We had to add int() function above because of the following issues:

    # if the user inputs 1 as number => input() function will make "1" as a string
    # because input function will always return a string data type

    # 3 it will be a string of "3"
    # 4 it will be a string of "4"
    # In such case, when we compare: if formula == 4 ("4"==4) this will be "False"
    # because we are comparing 4 as a string to 4 as a number
    # The solutions:
    # First solution: to convert the string into int insistently in the same line using int() function/method
    # Second solution: to change our if conditions to be like this: if formula=="1"

    # JS Review and Py quick note:
    # in JS we have == or ===
    # (3=="3") ==> True compare as values
    # (3==="3") ==> False compare as values and data type (Not in Python)
    # In python we have only == to compare both: the values and the data type

    # We will create 4 different functions for each formula (operation)
    # Step 3: use if conditions to call the right function
    result = 0
    if formula == 1:
        # call the total() function
        # In Python, we need to declare/create our functions before calling them
        # in other word, the function block has to be placed before calling it
        # and that's we are importing our functions before starting using them
        result = total(numbers_list)
        print(Fore.GREEN+"The total of your numbers is: ", result)
    elif formula == 2:
        # call the average() function
        result = average(numbers_list)
        print(Fore.GREEN+"The average of your numbers is: ", result)
    elif formula == 3:
        # call the max function
        print(Fore.GREEN+"max")
    elif formula == 4:
        # call the min function
        print(Fore.GREEN+"min")
    elif formula == 5:
        # call the min function
        print(Fore.GREEN+"Thank you, see you again!")
    else:
        print(Fore.Red+"Please enter a valid option number next time: 1, 2, 3, or 4")

# the end of while block
