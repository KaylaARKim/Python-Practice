# The python program testing the valid password
# Author: Kayla Ahreum Kim
# Date Created: 20/07/2021

# User input
def enterPassword():
    pw = input('Enter a string for password: ')
    analysePW(pw)

# Analyse password's valid
def analysePW(pw):
    # Let variables for analyse password
    characters = len(pw)
    numbers = sum(n.isdigit() for n in pw)
    letters = sum(l.isalpha() for l in pw)
    others = len(pw) - numbers - letters

    # Analyse password that user input
    if characters >= 8:
        if others == 0:
            if letters < 2:
                print()
                print('invalid password')
                print('Password must contain at least two letters.')
                print()
                enterPassword()

            elif numbers < 2:
                print()
                print('invalid password')
                print('Password must contain at least two numbers.')
                print()
                enterPassword()

            else:
                print()
                print('valid password')

        else:
            print()
            print('invalid password')
            print('Password must consist of only letters and digits')
            print()
            enterPassword()

    else:
        print()
        print('invalid password')
        print('Password must have at least eight characters.')
        print()
        enterPassword()

# Main (Call def enterPassword())
def main():
    enterPassword()

# Call main()
main()

