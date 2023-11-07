#method overloading
class Calculation:
    def add(self,a:int,b:int):
        print(a+b)
    def add(self,a:int,b:int,c:int):
        print(a+b+c)
def add(self,a:int,b:int,c:int=0):
        print(a + b + c)
cal=Calculation()
cal.add(1,2,3)

#method overriding
class Employee:
    __amt =20000
    def sal(self):
        return self.__amt*12
class ContractEmployee(Employee):
    __hrspay = 1000
    __hrs = 10
    def sal(self):
        return self.__hrspay *self.__hrs
emp=ContractEmployee()
print(emp.sal())

