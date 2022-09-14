class Employee:
        def __init__(self,name):
            institute_name=self.name
        def show(self):
            print(self.instutute_name)

class Employee1(Employee):
    def __init__(self,name,salary):
        emp_name=self.name
        salary=self.salary
    def show(self):
        print(self.salary)
        print()

em=Employee("Ram")
em1=Employee1("raj",1000)