# SubClass of Employee Management System
# Author: Kayla Ahreum Kim
# Date Created: 30/8/2021

from superClassEmployee import Employee

class ShiftEmployee(Employee):
    def __init__(self, idNo, name, department, jobTitle, shiftNo, payRate):
        super().__init__(idNo, name, department, jobTitle)
        self.__shiftNo = shiftNo
        self.__payRate = payRate

    def set_shiftNo(self, shiftNo):
        self.__shiftNo = shiftNo

    def set_payRate(self, payRate):
        self.__payRate = payRate

    def get_shiftNo(self):
        return self.__shiftNo

    def get_payRate(self):
        return self.__payRate
