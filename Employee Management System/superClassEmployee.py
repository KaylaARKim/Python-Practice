# SuperClass of Employee Management System
# Author: Kayla Ahreum Kim
# Date Created: 23/8/2021

class Employee:
    def __init__(self, idNo, name, department, jobTitle):
        self.__idNo = idNo
        self.__name = name
        self.__department = department
        self.__jobTitle = jobTitle


    def set_idNo(self, idNo):
        self.__idNo = idNo

    def set_name(self, name):
        self.__name = name

    def set_department(self, department):
        self.__department = department

    def set_jobTitle(self, jobTitle):
        self.__jobTitle = jobTitle


    def get_idNo(self):
        return self.__idNo

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_jobTitle(self):
        return self.__jobTitle




