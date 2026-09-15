class employee:
    def __init__(self,name,salary):
        self.name = name

        self.salary = salary


    def calculate_salary(self):
        return self.salary

        
class developer(employee):
    def calculate_salary(self):
        bonus = self.salary*0.20

        return self.salary + bonus




class manager(employee):

    def calculate_salary(self):
        bonus = self.salary*0.30

        return  self.salary +bonus

d = developer("SHIV ",55000)
m = manager("RAAYA ", 70000)

print(d.name, d.calculate_salary())
print(m.name, m.calculate_salary())
