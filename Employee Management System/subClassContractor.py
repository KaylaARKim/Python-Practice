# SubClass of Employee Management System
# Author: Kayla Ahreum Kim
# Date Created: 30/8/2021

from superClassEmployee import Employee

class Contractor(Employee):
    def __init__(self, idNo, name, department, jobTitle, contractEndDate, abn, contractSalary):
        super().__init__(idNo, name, department, jobTitle)
        self.__contractEndDate = contractEndDate
        self.__abn = abn
        self.__contractSalary = contractSalary

    def set_contractEndDate(self, contractEndDate):
        self.__contractEndDate = contractEndDate

    def set_abn(self, abn):
        self.__abn = abn

    def set_contractSalary(self, contractSalary):
        self.__contractSalary = contractSalary

    def get_contractEndDate(self):
        return self.__contractEndDate

    def get_abn(self):
        return self.__abn

    def get_contractSalary(self):
        return self.__contractSalary