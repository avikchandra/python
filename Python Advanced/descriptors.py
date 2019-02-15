class EmployeeDescriptor(object):

    def __get__(self,obj,owner):
        return self.__empname

    def __set__(self,obj,value):
        
        if not isinstance (value, str):
            raise TypeError("'empname' must be string.")

        self.__empname = value

class EmpIdDescriptor(object):

    def __get__(self,obj,owner):
        return self.__empid

    def __set__(self,obj,value):

        if hasattr(obj,'empid'):
            raise TypeError("'empid' is readonly attribute.")
        if not isinstance(value,int):
            raise TypeError("'empid' must be an integer.")

        self.__empid = value


class Employee(object):
    empid = EmpIdDescriptor()
    empname = EmployeeDescriptor()

    def __init__(self,emp_id,emp_name):
        self.empid = emp_id
        self.empname = emp_name


e1 = Employee(12345,"John")
print(e1.empid, '-', e1.empname)

e1.empname = "Doe"
print(e1.empid, '-', e1.empname)




