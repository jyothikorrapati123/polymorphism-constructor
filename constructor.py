#default:
class Employee:
    def fullname(self,fname,lname):
        print(fname+lname)
emp = Employee()
emp.fullname("vinay","kumar")
#parameter less constructor
class Employee:
    def __init__(self):
        pass
    def fullname(self,fname,lname):
        print(fname+lname)
    emp=Employee()
    emp.fullname("vinay","kumar")
#parameterized constructor
class Employee:
    __fName : str =("")
    __lName : str =("")
    def __init__(self,fName,lName):
        self.__fname = fName
        self.__lName =lName
    def fullName(self):
        print(self.__fname +self.__lName)
emp=Employee("vinay","kumar")
emp.fullName()


