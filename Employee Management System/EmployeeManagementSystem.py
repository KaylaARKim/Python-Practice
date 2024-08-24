# Python program save employee information and display it
# Author: Kayla Ahreum Kim
# Date Created: 18/8/2021

from subClassShiftEmployee import ShiftEmployee
from superClassEmployee import Employee
from subClassContractor import Contractor
import os.path
import pickle

# enter the information of contractor
def menu5_contractor(employeeList):
    try:
        # enter employee ID and using this as a key and find it's index
        inputID = int(input('Please enter the employee ID: '))
        idIndex = list(employeeList.keys()).index(inputID)
        i = idIndex

        # find other information and input other details of contractor
        cEmployeeID = list(employeeList.keys())[i]
        cEmployeeName = list(employeeList.values())[i][0]
        cEmployeeDepartment = list(employeeList.values())[i][1]
        cEmployeeJobTitle = list(employeeList.values())[i][2]
        cEndDate = input('Enter contract end date(yymmdd): ')
        cABN = int(input('Enter ABN(no space): '))
        cSalary = float(input('Enter contract salary: '))

        # matching the information to subclass
        contractorInfo = Contractor(cEmployeeID, cEmployeeName, cEmployeeDepartment, cEmployeeJobTitle, cEndDate, cABN,
                                    cSalary)

        # print the information that user input
        print()
        print('Employee ID: ', contractorInfo.get_idNo())
        print('Name: ', contractorInfo.get_name())
        print('Department: ', contractorInfo.get_department())
        print('Job Title: ', contractorInfo.get_jobTitle())
        print('Contract End Date: ', contractorInfo.get_contractEndDate())
        print('ABN: ', contractorInfo.get_abn())
        print('Contract Salary: ', contractorInfo.get_contractSalary())

    except Exception as exception:
        print('You entered wrong information.')
        print('Try again.')
        menu5_contractor(employeeList)


# delete employee information
def menu4_delete(employeeList):
    try:
        # enter employee ID and using this as a key and delete key and values
        print()
        delID = int(input('Please enter the employee ID that you want to delete: '))

        if delID in employeeList:
            del employeeList[delID]
            print()
            print(f'Employee with employee id {delID} has been deleted.')

        elif delID not in employeeList:
            print('You entered wrong information.')
            print('Try again.')
            menu4_delete(employeeList)

    except Exception as e:
        print('There is an error')
        print(e)

# add employee information
def menu3_add(employeeList):
    try:
        # enter employee ID and using this as a key and add key and values
        print()
        newID = int(input('Please enter the employee ID: '))

        # input employee information
        if newID not in employeeList:
            newName = str(input('Please enter the employee name: '))
            newDepartment = str(input('Please enter the department: '))
            newJobTitle = str(input('Please enter the job title: '))
            print('Please enter the number(only 1 or 2)')
            print('1. Day Shift      2. Night Shift')
            newShiftNo = int(input(': '))
            newPayRate = float(input('Please enter the pay rate: '))

            if newShiftNo == 1:
                newShift = 'Day'
            elif newShiftNo == 2:
                newShift = 'Night'

            # make dictionary by using input information
            employeeList[newID] = [newName, newDepartment, newJobTitle, newShift, newPayRate]

            idIndex = list(employeeList.keys()).index(newID)
            i = idIndex

            employeeID = list(employeeList.keys())[i]
            employeeName = list(employeeList.values())[i][0]
            employeeDepartment = list(employeeList.values())[i][1]
            employeeJobTitle = list(employeeList.values())[i][2]
            employeeShift = list(employeeList.values())[i][3]
            employeePayRate = list(employeeList.values())[i][4]

            # matching the information to subclass
            employeeInfo = ShiftEmployee(employeeID, employeeName, employeeDepartment, employeeJobTitle, employeeShift, employeePayRate)

            # print the information that user input
            print()
            print('New employee\'s information has been updated.')

            print('Employee ID: ', employeeInfo.get_idNo())
            print('Name: ', employeeInfo.get_name())
            print('Department: ', employeeInfo.get_department())
            print('Job Title: ', employeeInfo.get_jobTitle())
            print('Shift: ', employeeInfo.get_shiftNo())
            print('Hourly Pay Rate: ', employeeInfo.get_payRate())

        else:
            print('Already exist')

    except Exception as exception:
        print('You entered wrong information.')
        print('Try again.')
        menu3_add(employeeList)


# change employee information
def menu2_change(employeeList):
    try:
        # enter employee ID and using this as a key and change key or values
        print()
        modifyID = int(input('Please enter the employee ID that you want to change: '))

        # input employee information
        if modifyID in employeeList:
            modifyName = str(input('Please enter the employee name: '))
            modifyDepartment = str(input('Please enter the department: '))
            modifyJobTitle = str(input('Please enter the job title: '))
            print('Please enter the number(only 1 or 2)')
            print('1. Day Shift      2. Night Shift')
            modifyShiftNo = int(input(': '))
            modifyPayRate = float(input('Please enter the pay rate: '))

            if modifyShiftNo == 1:
                modifyShift = 'Day'
            elif modifyShiftNo == 2:
                modifyShift = 'Night'

            # make dictionary by using input information
            employeeList[modifyID] = [modifyName, modifyDepartment, modifyJobTitle, modifyShift, modifyPayRate]

            idIndex = list(employeeList.keys()).index(modifyID)
            i = idIndex

            employeeID = list(employeeList.keys())[i]
            employeeName = list(employeeList.values())[i][0]
            employeeDepartment = list(employeeList.values())[i][1]
            employeeJobTitle = list(employeeList.values())[i][2]
            employeeShift = list(employeeList.values())[i][3]
            employeePayRate = list(employeeList.values())[i][4]

            # matching the information to subclass
            employeeInfo = ShiftEmployee(employeeID, employeeName, employeeDepartment, employeeJobTitle, employeeShift, employeePayRate)

            # print the information that user input
            print()
            print('Employee\'s information has been updated.')
            print('Employee ID: ', employeeInfo.get_idNo())
            print('Name: ', employeeInfo.get_name())
            print('Department: ', employeeInfo.get_department())
            print('Job Title: ', employeeInfo.get_jobTitle())
            print('Shift: ', employeeInfo.get_shiftNo())
            print('Hourly Pay Rate: ', employeeInfo.get_payRate())
        else:
            print('ID NOT FOUND')

    except Exception as exception:
        print('You entered wrong information.')
        print('Try again.')
        menu2_change(employeeList)

# find employee information
def menu1_find(employeeList):
    try:
        # enter employee ID and using this as a key and change key or values
        print()
        inputID = int(input('Please enter the employee ID: '))
        idIndex = list(employeeList.keys()).index(inputID)
        i = idIndex

        employeeID = list(employeeList.keys())[i]
        employeeName = list(employeeList.values())[i][0]
        employeeDepartment = list(employeeList.values())[i][1]
        employeeJobTitle = list(employeeList.values())[i][2]
        employeeShift = list(employeeList.values())[i][3]
        employeePayRate = list(employeeList.values())[i][4]

        # matching the information to subclass
        employeeInfo = ShiftEmployee(employeeID, employeeName, employeeDepartment, employeeJobTitle, employeeShift, employeePayRate)

        # print the information that user input
        print()
        print('Employee ID: ', employeeInfo.get_idNo())
        print('Name: ', employeeInfo.get_name())
        print('Department: ', employeeInfo.get_department())
        print('Job Title: ', employeeInfo.get_jobTitle())
        print('Shift: ', employeeInfo.get_shiftNo())
        print('Hourly Pay Rate: ', employeeInfo.get_payRate())

    except Exception as exception:
        print('You entered wrong information.')
        print('Try again.')
        menu1_find(employeeList)


# print menu
def menu(employeeList):
    try:
        # print menu and input number
        print()
        print('-------------------------------------------')
        print('                   MENU                    ')
        print('-------------------------------------------')
        print('1. Find employee by employee ID')
        print('2. Change the information of employee')
        print('3. Add the information of employee')
        print('4. Delete the information of employee')
        print('5. Contractor')
        print('6. Exit')

        print()
        inputMenu = int(input('Please choose the number: '))

        # navigate menu
        if inputMenu == 1:
            showEmployeeID(employeeList)
            menu1_find(employeeList)
            menu(employeeList)

        elif inputMenu == 2:
            showEmployeeID(employeeList)
            menu2_change(employeeList)
            menu(employeeList)

        elif inputMenu == 3:
            showEmployeeID(employeeList)
            menu3_add(employeeList)
            menu(employeeList)

        elif inputMenu == 4:
            showEmployeeID(employeeList)
            menu4_delete(employeeList)
            menu(employeeList)

        elif inputMenu == 5:
            showEmployeeID(employeeList)
            menu5_contractor(employeeList)
            menu(employeeList)

        elif inputMenu == 6:
            with open('employeeInformation.p', 'wb') as file:
                pickle.dump(employeeList, file)
            exit()

        else:
            print()
            print('You enter the wrong number.')
            print('Enter the number again.')
            menu(employeeList)

    except Exception as exception:
        print('You entered wrong information.')
        print('Try again.')
        menu(employeeList)


# show the list of Employee ID that system already has
def showEmployeeID(employeeList):
    try:
        print()
        print('Employee ID that system already has')
        countKeys = len(employeeList.keys())

        for i in range(countKeys):
            keyList = list(employeeList.keys())[i]
            print(f'- {keyList}')

    except Exception as exception:
        print(exception)
        exit()


# input the shift and pay rate
def input_Shift_PayRate(employeeList):
    try:

        countKeys = len(employeeList.keys())
        for i in range(countKeys):
            employeeID = list(employeeList.keys())[i]
            print()
            print(f'Please input information of shift and pay rate of {employeeID}')
            print()
            print('Enter the number(1 or 2)')
            print('1. Day Shift      2. Night Shift')
            shiftNo = int(input(': '))
            payRate = float(input('Please enter you hourly pay rate: '))

            if shiftNo == 1:
                shift = 'Day'
            elif shiftNo == 2:
                shift = 'Night'

            idIndex = list(employeeList.keys()).index(employeeID)
            i = idIndex

            employeeValuesAddShift = employeeList[employeeID].append(shift)
            employeeValuesAddPayRate = employeeList[employeeID].append(payRate)

            employeeID = list(employeeList.keys())[i]
            employeeName = list(employeeList.values())[i][0]
            employeeDepartment = list(employeeList.values())[i][1]
            employeeJobTitle = list(employeeList.values())[i][2]
            employeeShift = list(employeeList.values())[i][3]
            employeePayRate = list(employeeList.values())[i][4]

            employeeInfo = ShiftEmployee(employeeID, employeeName, employeeDepartment, employeeJobTitle, employeeShift,
                                         employeePayRate)

            print()
            print('Employee ID: ', employeeInfo.get_idNo())
            print('Name: ', employeeInfo.get_name())
            print('Department: ', employeeInfo.get_department())
            print('Job Title: ', employeeInfo.get_jobTitle())
            print('Shift: ', employeeInfo.get_shiftNo())
            print('Hourly Pay Rate: ', employeeInfo.get_payRate())

        menu(employeeList)

    except Exception as exception:
        print('You entered wrong information.')
        print('Try again.')
        input_Shift_PayRate(employeeList)


# find file and read or write file
def findFile():
    employee1, employee2, employee3 = storedEmployee()

    try:
        if os.path.isfile('employeeInformation.p'):
            with open('employeeInformation.p', 'rb') as file:
                employeeList = pickle.load(file)
        else:
            employeeList = {employee1.get_idNo(): [employee1.get_name(), employee1.get_department(),
                                                   employee1.get_jobTitle()],
                            employee2.get_idNo(): [employee2.get_name(), employee2.get_department(),
                                                   employee2.get_jobTitle()],
                            employee3.get_idNo(): [employee3.get_name(), employee3.get_department(),
                                                   employee3.get_jobTitle()]}

            with open('employeeInformation.p', 'wb') as file:
                pickle.dump(employeeList, file)

            with open('employeeInformation.p', 'rb') as file:
                employeeList = pickle.load(file)

        firstKey = list(employeeList.values())[0]
        countFirstKey = len(firstKey)

        if countFirstKey == 5:
            menu(employeeList)
        elif countFirstKey == 3:
            input_Shift_PayRate(employeeList)

    except Exception as exception:
        print(exception)
        exit()


# employee information
def storedEmployee():
    employee1 = Employee(47899, 'Susanna Myer', 'Accounting', 'Vice President')
    employee2 = Employee(39119, 'Mark Joseph', 'Info Tech', 'Programmer')
    employee3 = Employee(81774, 'Joyce Roberts', 'Manufacturing', 'Engineer')

    return employee1, employee2, employee3


def main():
    findFile()


main()
