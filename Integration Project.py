# Chance Mullen
# Integration project

# Sprint 1

# print("When you want to manipulate integers or floats you can use the following operators as shown with these examples.")
# x = 10
# y = 5
# print(x * y), print("This prints '50' because it evaluates 5 times 10")
# print(x ** y), print("This prints '100000' because it evaluates 10 to the 5th power.")
# print(x / y), print("This prints5 '2.0' because it evaluated 10 divided by 5 and returns a float.")
# print(x % y), print("This prints '0' because there is no remainder.")
# print(x // y), print("This prints '2' because it prints the answer without the remainder.")
# print(x + y), print("This prints '15' because it adds the 2 values '10' and '5' together.")
# print(x - y), print("This prints '5' because it subtracts 5 from 10.")
# print()

# String operators
# print("When you want to mess with strings")
# x = "Good-bye"

# This will print 'Hello' 10 times with no spaces. Any string multiplied by an integer will have a similar result.
# print("Hello" * 10)

# This prints 'Hello Good-bye' because it concatenates the strings.
# print("Hello you're one of: " + x)
# print()

# Assignment operators
# print("If you want to store a number or a string as a variable you can use input() or int()")

# This prompts the user to enter a word to be stored in the variable 'word'
# word = input("Enter a word: ")

# This prompts the user to enter a number to be stored as an integer.
# number = int(input("Enter a number: "))
# print(word, number)
# print()

# End

###############################################################
# Sprint 2

# In python you can test a conditional statement with If, if-else, if-elif, and if-elif-else statements
# I will be demonstrating these using the following lists:

list1 = [1, 2, 2, 3, 4, 5, 6, 9]
list2 = [2, 2, 3, 5, 4, 7, 7, 9]

# This for loop tests the 3 conditional statements 8 times in
# total (0 to 8) and prints each result on a different line.
# for i in range(8):
    # This if statement uses the relational operator == to test if
    # the element in the same position in each list is equal
#     if list1[i] == list2[i]:
#        print(str(list1[i]) + " is equal to " + str(list2[i]))

    # This if statement uses the relational operator > to test if the element
    # in the same position in list 1 is larger than the one in list 2.
#    elif list1[i] > list2[i]:
#        print(str(list1[i]) + " is larger than " + str(list2[i]))

    # This will execute when neither the if or elif statement is satisfied.
    # It can be assumed if the number is not equal or larger, it is smaller.
#    else:
#        print(str(list1[i]) + " is smaller than " + str(list2[i]))
#    print(' ')

# print("The results above are a result of using;")
# print("A for-loop to check all 8 elements in the lists.")
# print("An if statement to check equality and an elif statement to check if #1 is larger than #2")
# print("Overall, I used en if-elif-else statement to tests all 3 possibilities between the two numbers.")

# It is also useful to use the boolean operators 'not', 'and', and 'or'.
# These can be tested in if conditionals and use with while loops.
# For example:
# z = None
# list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# while z != 0:
#    for i in range(10):
#        z = list3[i]
#        if not(list3[i] > list3[i-1]) and list3[i] < 10:
#            print(str(list3[i]) + " is larger than " + str(list3[i-1]) + " and " + str(list3[i]) + " is less than 10")
#            print("This is the only time this is true")
#            print(' ')
#        elif list3[i] >= 0 or list3[i] < 10:
#            print(str(list3[i]) + " is atleast 0 or " + str(list3[i]) + " is less than 10")
#            print("This will always be true")
#            print(' ')

# print("The results above show the use of a while-loop, it will run until z = 0, which is the last number in the list")
# print("To test the conditions I used 'and' and 'or' booleans.")
# print("The 'and' boolean returns true if both statements are true, while or returns true if at least one is true.")
# print("Each time 'This is always true' and 'This is the only time this is true' is printed, the boolean returned true.")

# I use the function definition below in my program.

# End

##################################################################################################
# Chance Mullen
# 2019/2020 Premier league top 6 information

# The goal of this program is to get statistics for any team
# in the premier league top 6 at the end of the 2019/2020 season.
# ## Information is from fotmob.com and the official Premier league website.
# Welcome message and instructions


def main():
    teams = [" ", "Liverpool", "Manchester City", "Manchester United", "Chelsea", "Leicester City", "Tottenham Hostpur"]
    team_points = [0, 99, 81, 66, 66, 62, 59]
    print("Welcome to my program"), print(" ")
    print("The top 6 teams are: ")
    for i in range(1, 7):
        print(str(i) + ": " + str(teams[i]) + "  " + "pts:[" + str(team_points[i]) + "]")


main()

