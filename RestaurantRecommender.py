# The python program that recommend the restaurant
# Author: Kayla Ahreum Kim
# Date Created: 20/07/2021

import turtle as t

wn = t.Screen()
t.hideturtle()
t.bgcolor('skyblue')

# Make restaurant's list
def chooseRestaurant(vegeAns, veganAns, glutenFreeAns):
    first = 'Joe\'s Gourmet Burgers'
    second = 'Main Street Pizza Company'
    third = 'Corner Cafe'
    fourth = 'Mama\'s Fine Italian'
    fifth = 'The Chef\'s Kitchen'

    if vegeAns == 'YES':
        if veganAns == 'YES':
            if glutenFreeAns == 'YES':
                t.write('Here are your restaurant choices:')
                t.forward(15)
                t.write('\t{0:}' .format(third))
                t.forward(15)
                t.write('\t{0:}' .format(fifth))

            elif glutenFreeAns == 'NO':
                t.write('Here are your restaurant choices:')
                t.forward(15)
                t.write('\t{0:}' .format(third))
                t.forward(15)
                t.write('\t{0:}' .format(fifth))

            else:
                t.write('Please answer only yes or no')
                t.forward(20)
                userAns()

        elif veganAns == 'NO':
            if glutenFreeAns == 'YES':
                t.write('Here are your restaurant choices:')
                t.forward(15)
                t.write('\t{0:}' .format(second))
                t.forward(15)
                t.write('\t{0:}' .format(third))
                t.forward(15)
                t.write('\t{0:}' .format(fifth))

            elif glutenFreeAns == 'NO':
                t.write('Here are your restaurant choices:')
                t.forward(15)
                t.write('\t{0:}' .format(second))
                t.forward(15)
                t.write('\t{0:}' .format(third))
                t.forward(15)
                t.write('\t{0:}' .format(fourth))
                t.forward(15)
                t.write('\t{0:}' .format(fifth))

            else:
                t.write('Please answer only yes or no')
                t.forward(20)
                userAns()

        else:
            t.write('Please answer only yes or no')
            t.forward(20)
            userAns()

    elif vegeAns == 'NO':
        if veganAns == 'YES':
            if glutenFreeAns == 'YES':
                t.write('Here are your restaurant choices:')
                t.forward(15)
                t.write('\t{0:}' .format(third))
                t.forward(15)
                t.write('\t{0:}' .format(fifth))

            elif glutenFreeAns == 'NO':
                t.write('Here are your restaurant choices:')
                t.forward(15)
                t.write('\t{0:}' .format(third))
                t.forward(15)
                t.write('\t{0:}' .format(fifth))

            else:
                t.write('Please answer only yes or no')
                t.forward(20)
                userAns()

        elif veganAns == 'NO':
            if glutenFreeAns == 'YES':
                t.write('Here are your restaurant choices:')
                t.forward(15)
                t.write('\t{0:}' .format(second))
                t.forward(15)
                t.write('\t{0:}' .format(third))
                t.forward(15)
                t.write('\t{0:}' .format(fifth))

            elif glutenFreeAns == 'NO':
                t.write('Here are your restaurant choices:')
                t.forward(15)
                t.write('\t{0:}' .format(first))
                t.forward(15)
                t.write('\t{0:}' .format(second))
                t.forward(15)
                t.write('\t{0:}' .format(third))
                t.forward(15)
                t.write('\t{0:}' .format(fourth))
                t.forward(15)
                t.write('\t{0:}' .format(fifth))

            else:
                t.write('Please answer only yes or no')
                t.forward(20)
                userAns()

        else:
            t.write('Please answer only yes or no')
            t.forward(20)
            userAns()

    else:
        t.write('Please answer only yes or no')
        t.forward(20)
        userAns()

# Print questions and answers
def showAns(vegeAns, veganAns, glutenFreeAns):
    t.penup()
    t.setheading(-90)

    t.write('Is anyone in your party a vegetarian? {0:}' .format(vegeAns))
    t.forward(15)
    t.write('Is anyone in your party a vegan? {0:}' .format(veganAns))
    t.forward(15)
    t.write('Is anyone in your party a gluten-free? {0:}' .format(glutenFreeAns))
    t.forward(15)

    chooseRestaurant(vegeAns, veganAns, glutenFreeAns)

# Ask questions (User inputs)
def userAns():
    vegeAns = t.textinput('Input', 'Is anyone in your party a vegetarian?\n(please answer only yes or no)')
    veganAns = t.textinput('Input', 'Is anyone in your party a vegan?\n(please answer only yes or no)')
    glutenFreeAns = t.textinput('Input', 'Is anyone in your party a gluten-free?\n(please answer only yes or no)')

    # Make user inputs capital letter
    vegeAns = vegeAns.upper()
    veganAns = veganAns.upper()
    glutenFreeAns = glutenFreeAns.upper()

    showAns(vegeAns, veganAns, glutenFreeAns)

# Main (Call def userAns())
def main():
    userAns()

# Call main()
main()

t.mainloop()

