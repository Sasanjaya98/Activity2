class Employee:
    x = 10 
 
    def func_msg(self):
         print('Welcome to Employee Class')
 
class Department(Employee):
    a = 250

    def func_message(self):
        print('Welcome to Department Class')
        print('This class is inherited from Employee')
 
emp = Employee()
print(emp.x)
emp.func_msg()