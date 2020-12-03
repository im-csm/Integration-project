# Chance Mullen
# Integration project

"""
# Sprint 1

print("When you want to manipulate integers or floats you can use the following
 operators as shown with these examples.")
x = 10
y = 5
print(x * y)
print("This prints '50' because it evaluates 5 times 10")
print(x ** y)
print("This prints '100000' because it evaluates 10 to the 5th power.")
print(x / y)
print("This prints5 '2.0' because it evaluated 10 divided by 5 and returns a
float.")
print(x % y)
print("This prints '0' because there is no remainder.")
print(x // y)
print("This prints '2' because it prints the answer without the remainder.")
print(x + y)
print("This prints '15' because it adds the 2 values '10' and '5' together.")
print(x - y)
print("This prints '5' because it subtracts 5 from 10.")
print()

# String operators
print("When you want to mess with strings:"), print()
x = "Good-bye"

# This will print 'Hello' 10 times with no spaces. Any string multiplied by an
integer will have a similar result.
print("Multiplying a string by an integer does this:"), print("Hello" * 10)

# This prints 'Hello Good-bye' because it concatenates the strings.
print("Hello " + x)
print("You can concatenate strings variables that are also strings")

# Assignment operators
print("If you want to store a number or a string as a variable you can use
input() or int()")

# This prompts the user to enter a word to be stored in the variable 'word'
word = "Hello"
print('word = "Hello"')

# This prompts the user to enter a number to be stored as an integer.
number = 77
print('number = 77')
print(word, number)
print(), print("--------------------------------------------------------")

# End
"""
###############################################################

"""
# Sprint 2

# In python you can test a conditional statement with If, if-else, if-elif, 
and if-elif-else statements
# I will be demonstrating these using the following lists:

list1 = [1, 2, 2, 3, 4, 5, 6, 9]
list2 = [2, 2, 3, 5, 4, 7, 7, 9]

# This for loop tests the 3 conditional statements 8 times in
# total (0 to 8) and prints each result on a different line.
for i in range(8):
    # This if statement uses the relational operator == to test if
    # the element in the same position in each list is equal
    if list1[i] == list2[i]:
        print(str(list1[i]) + " is equal to " + str(list2[i]))

    # This if statement uses the relational operator > to test if the element
    # in the same position in list 1 is larger than the one in list 2.
    elif list1[i] > list2[i]:
        print(str(list1[i]) + " is larger than " + str(list2[i]))

    # This will execute when neither the if or elif statement is satisfied.
    # It can be assumed if the number is not equal or larger, it is smaller.
    else:
        print(str(list1[i]) + " is smaller than " + str(list2[i]))
    print(' ')

print("The results above are a result of using;")
print("- A for-loop to check all 8 elements in the lists.")
print("- An if statement to check equality and an elif statement to check if 
#1 is larger than #2")
print("Overall, I used an if-elif-else statement to test all 3 possibilities 
between the two numbers.")
print()

# It is also useful to use the boolean operators 'not', 'and', and 'or'.
# These can be tested in if conditionals and use with while loops.
# For example:
z = None
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
while z != 0:
    for j in range(10):
        z = list3[j]
        if not(list3[j] > list3[j-1]) and list3[j] < 10:
            print(str(list3[j]) + " is larger than " + str(list3[j-1]) + " and
             " + str(list3[j]) + " is less than 10")
            print("This is the only time this is true")
            print("This is because 0 is not larger than 9, but the condition 
            returns the opposite with 'not' so it returns true.")
            print(' ')
        elif list3[j] >= 0 or list3[j] < 10:
            print(str(list3[j]) + " is at least 0 or " + str(list3[j]) +
            " is less than 10")
            print("This will always be true")
            print(' ')

print("The results above show the use of a while-loop, it will run until z = 0,
 which is the last number in the list")
print("To test the conditions I used 'and' and 'or' booleans.")
print("The 'and' boolean returns true if both statements are true, while or 
returns true if at least one is true.")
print("Each time 'This is always true' and 'This is the only time this is true' 
is printed, the boolean returned true.")

# I use the function definition below in my program.

# End
"""
###############################################################################
"""
019/2020 Premier league top 6 information

The goal of this program is to get statistics for any team that finished
in the top 6 at the end of the 2019/2020 Premier League season.
Information is from fotmob.com and the official Premier league website.
I created this for a project in my Intro to Computer Science course at FGCU,
and it is my first ever "complete" python program!
"""
__author__ = "Chance Mullen"
global choice, teamname, ask, z


def main():
    print("""
Welcome to my program about the Premier league's top 6 teams from 2019/2020!
The top 6 teams were:
""")
    choices()


def restart_it():
    """The purpose of this function is to restart the program without giving
    the starting message again."""
    import sys
    import os
    global teamname
    print("The top 6 teams were:")
    print()
    teams = [" ", "Liverpool", "Manchester City", "Manchester United",
             "Chelsea", "Leicester City", "Tottenham Hotspur"]
    team_points = [0, 99, 81, 66, 66, 62, 59]
    print()
    for i in range(1, 7):
        print(str(i) + ": " + str(teams[i]) + "  " + "pts:[" + str(
            team_points[i]) + "]")
    check3 = 0
    while check3 == 0:
        print()
        teamname = (input("Enter another team name, or the same team name for "
                          "different options: "))
        print()
        try:
            file_name = (teamname + "/" + teamname + '.txt')
            s = open(os.path.join(sys.path[0], file_name), 'r')
            team_selection = s.read()
            print(team_selection)
            check3 += 1
        except (OSError, IOError):
            print("That is not a correct team name.")
    options = ['Record', 'Last 5', 'Starting 11', 'Club History']
    """"""
    print("I can tell you more about the following topics for " +
          teamname + ';\n')
    for x in range(1, 5):
        print(str(x) + '. ' + options[x - 1])
    print()
    team_info(teamname)


def choices():
    """The purpose of this function is to provide the user with the list of
    team names and allow them to choose one of them to learn more about.
    """
    import sys
    import os
    global teamname
    teams = [" ", "Liverpool", "Manchester City", "Manchester United",
             "Chelsea", "Leicester City", "Tottenham Hotspur"]
    team_points = [0, 99, 81, 66, 66, 62, 59]
    for i in range(1, 7):
        print(str(i) + ": " + str(teams[i]) + "  " + "pts:[" + str(
            team_points[i]) + "]")
    checker = 0
    while checker == 0:
        print()
        teamname = (input("Enter the name of a team from above: "))
        print()
        try:
            file_name = (teamname + "/" + teamname + '.txt')
            s = open(os.path.join(sys.path[0], file_name), 'r')
            team_selection = s.read()
            print(team_selection)
            checker += 1
        except (OSError, IOError):
            print("That is not a correct team name.")
    options = ['Record', 'Last 5', 'Starting 11', 'Club History']
    """"""
    print("I can tell you more about the following topics for " +
          teamname + ';\n')
    for x in range(1, 5):
        print(str(x) + '. ' + options[x - 1])
    print()
    team_info(teamname)


def team_info(team_name):
    """
    This function takes the name of a team and will provide the user with
    new options they can choose from to learn more about their selected
    team.
    """
    import sys
    import os
    global choice, z, ask
    info = ['Record', 'Last 5', 'Starting 11', 'Club History']
    check2 = 0
    while check2 == 0:
        print()
        choice = str(input("Pick what info you would like to know: "))
        if choice in info:
            txt_name = (team_name + "/")
            choice_name = (txt_name + choice + ".txt")
            s = open(os.path.join(sys.path[0], choice_name), 'r')
            info_selection = s.read()
            print()
            print(info_selection)
            print()
            check2 += 1
        else:
            print("That is not in the list.")
        z = 0
    while z == 0:
        l = str(input("Enter 'Y' to restart or 'N' to end the program: "))
        if l == 'Y' or l == 'y':
            restart_it()
        elif l == 'N' or l == 'n':
            z += 1
        else:
            print()
            print("Y or N please.")
    sys.exit("You have exited the program.")


main()
