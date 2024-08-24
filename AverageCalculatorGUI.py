# The python GUI program that calculate average score of 3 tests
# Author: Kayla Ahreum Kim
# Date Created: 20/9/2021

# Import tkinter
from tkinter import *
from tkinter import messagebox

# Calculate average of the scores
def average():
    try:
        # Define variables
        score1 = float(scoreFirst.get())
        score2 = float(scoreSecond.get())
        score3 = float(scoreThird.get())
        scoreAvg = float((score1 + score2 + score3) / 3)
        scoreAvg_entry.insert(0, scoreAvg)

    except:
        messagebox.showinfo('Wrong', 'Enter the number only')


# Create new window
window = Tk()

window.geometry("300x200")
window.title('Calculate Average')


# The label of each entry's information
score1_label = Label(window, text = "Enter the score for test 1:")
score1_label.grid(row = '1', column = '0', padx = 7, pady = 5)

score2_label = Label(window, text = "Enter the score for test 2:")
score2_label.grid(row = '2', column = '0', padx = 7, pady = 5)

score3_label = Label(window, text = "Enter the score for test 3:")
score3_label.grid(row = '3', column = '0', padx = 7, pady = 5)

scoreAvg_label = Label(window, text = "Average: ")
scoreAvg_label.grid(row = '4', column = '0', padx = 7, pady = 5)


# The entry for score that user input
scoreFirst = StringVar()
score1_entry = Entry(window, width = 13, textvariable = scoreFirst)
score1_entry.grid(row = '1', column = '1')

scoreSecond = StringVar()
score2_entry = Entry(window, width = 13, textvariable = scoreSecond)
score2_entry.grid(row = '2', column = '1')

scoreThird = StringVar()
score3_entry = Entry(window, width = 13, textvariable = scoreThird)
score3_entry.grid(row = '3', column = '1')


# The entry for show average of the scores
scoreAverage = StringVar()
scoreAvg_entry = Entry(window, width = 13, textvariable = scoreAverage)
scoreAvg_entry.grid(row = '4', column = '1', padx = 7, pady = 5)


# The button for calculate average
calAvg_button = Button(window, text = 'Average', width = 10, command = average)
calAvg_button.grid(row = '5', column = '0', pady = 5)


# The button for quit the program
quit_button = Button(window, text = 'Quit', width = 10, command = quit)
quit_button.grid(row = '5', column = '1', pady = 5)


window.mainloop()