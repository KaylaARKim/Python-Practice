# The python GUI program that calculate student’s grade that user input
# Author: Kayla Ahreum Kim
# Date Created: 30/8/2021

import tkinter
from tkinter import *
from tkinter import messagebox


# Calculate average score from list box
def calAvg():
    entAvg.delete(0, END)
    total = calTotal()
    avg = total / (len(scoreList) - 1)
    entAvg.insert(0, f'{avg:.2f}')

# Calculate total score from list box
def calTotal():
    entTotal.delete(0, END)
    lowest = analyzeLow()
    total = sum(scoreList) - lowest
    entTotal.insert(0, total)

    return total

# Find the lowest score in the list box
def analyzeLow():
    entLowest.delete(0, END)
    lowest = min(scoreList)
    entLowest.insert(0, lowest)

    return lowest

# Execute calculate total and average, find the lowest score all together
def calculate():
    if len(scoreList) == 10:
        analyzeLow()
        calTotal()
        calAvg()
    elif len(scoreList) != 10:
        messagebox.showinfo('Information','You should enter 10 numbers')

# reset all
def resetAll():
    lstScore.delete(0, END)
    entTotal.delete(0, END)
    entAvg.delete(0, END)
    entLowest.delete(0, END)
    scoreList.clear()

# delete selected user input score
def deleteScore():
    for i in lstScore.curselection():
        delNum = lstScore.get(i)
    lstScore.delete(ANCHOR)
    scoreList.remove(delNum)
    entTotal.delete(0, END)
    entAvg.delete(0, END)
    entLowest.delete(0, END)

# insert user input score to listbox
def insertScore():
    if len(scoreList) < 10:
        lstScore.insert(END, float(entTestScore.get()))
        scoreList.append(float(entTestScore.get()))
        print(scoreList)
        entScore.delete(0, END)

    elif len(scoreList) <= 10:
        messagebox.showinfo('Information','You should enter 10 numbers')

scoreList = []

window = Tk()

window.title("Student Grade Calculator")
window.geometry("380x410")

# Input score to list  box
lblScore = Label(window, width = 5, text = "Score")
lblScore.grid(row = 0, column = 0, columnspan = 2, padx = (10,0), pady = (20,0))

entTestScore = StringVar()
entScore = Entry(window, width = 20, textvariable = entTestScore)
entScore.grid(row = 0, column = 2, columnspan = 2, pady = (20,0))

btnScore = Button(window, width = 10, text = "Enter", command = insertScore)
btnScore.grid(row = 0, column = 4, columnspan = 2, pady = (20,0))

lstTestScore = StringVar()
lstScore = Listbox(window, height = 10, listvariable = lstTestScore)
lstScore.grid(row = 1, column = 2, columnspan = 2, pady = 20)

# delete selected button
btnDelete = Button(window, width = 15, text = "Delete Selected", command = deleteScore)
btnDelete.grid(row = 2, column = 2,  columnspan = 2)


# Analyze the lowest score
lblLowest = Label(window, text = 'The Lowest Score')
lblLowest.grid(row = 3, column = 0, columnspan = 2, padx = (10,0), pady = (20, 0))

entLowestNo = StringVar()
entLowest = Entry(window, width = 15, textvariable = entLowestNo)
entLowest.grid(row = 4, column = 0,  columnspan = 2, padx = (10,0))


# calculate total score
lblTotal = Label(window, text = 'Total Score')
lblTotal.grid(row = 3, column = 2,  columnspan = 2, pady = (10, 0))

entTotalNo = StringVar()
entTotal = Entry(window, width = 15, textvariable = entTotalNo)
entTotal.grid(row = 4, column = 2,  columnspan = 2)


# calculate average score
lblAvg = Label(window, text = 'Average Score')
lblAvg.grid(row = 3, column = 4,  columnspan = 2, pady = (10, 0))

entAvgNo = StringVar()
entAvg = Entry(window, width = 15, textvariable = entAvgNo)
entAvg.grid(row = 4, column = 4,  columnspan = 2)


# calculate and analyze score button
btnCalculate = Button(window, width = 15, text = "Calculate", command = calculate)
btnCalculate.grid(row = 5, column = 1,  columnspan = 2, pady = (20, 0))


# reset all of them button
btnReset = Button(window, width = 15, text = "Reset", command = resetAll)
btnReset.grid(row = 5, column = 3,  columnspan = 2, pady = (20, 0))

window.mainloop()
