# This is a sample Python script.
import re
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run = True
    while run:
        string = input("Please enter a string: ")
        subString = input("Please enter the substring you wish to find: ")
        replacement = input("Please enter a string to replace the given substring: ")
        x = re.sub(subString, replacement, string)
        print("Your new string is: " + x)
        done = input("You wish to continue? (enter 'yes'): ")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
